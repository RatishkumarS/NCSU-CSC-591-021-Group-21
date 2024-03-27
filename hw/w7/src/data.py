import math
from row import ROW
from num import NUM
from sym import SYM
from cols import COLS
from node import NODE
import random, sys, re
import numpy as np



class DATA:

    def __init__(self, src=[], fun=None):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            for _, x in self.csv(src):
                self.add(x, fun)
        else:
            self.add(src, fun)

    def csv(self, src):
        try:
            src = sys.stdin if src == "-" else open(src, "r")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {src}")
        with src:
            for i, line in enumerate(src, start=1):
                yield i, self.cells(line.strip())

    def cells(self, s):
        t = [self.coerce(s1) for s1 in s.split(",")]
        return t

    def coerce(self, s):
        def fun(s2):
            return (
                None
                if s2 == "null"
                else s2.lower() == "true" or (s2.lower() != "false" and s2)
            )

        try:
            return float(s) if s is not None else None
        except ValueError:
            return fun(re.match(r"^\s*(.*\S)", s).group(1)) if isinstance(s, str) else s

    def add(self, t, fun=None):
        row = t if isinstance(t, ROW) else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.cols.add(row)
            self.rows.append(row)
        else:
            self.cols = COLS(row)
    def rnd(n, ndecs=None):
        if not isinstance(n, (int, float)):
            return n
        if math.floor(n) == n:
            return n
        mult = 10 ** (ndecs or 2)
        return math.floor(n * mult + 0.5) / mult


    def mid(self, cols=None):
        u = [round(col.mid(), 2) for col in (cols or self.cols.all)]
        return ROW(u)

    def div(self, cols=None):
        u = [round(col.div(), 2) for col in (cols or self.cols.all)]
        return ROW(u)

    def stats(data):
        statistics = {}
        total_rows = max(col.n for col in data.cols.all)
        statistics[".N"] = total_rows
        for col in data.cols.all:
            if isinstance(col, NUM):
                mean = col.mid()
                statistics[f"{col.txt}"] = round(mean, 2)
            elif isinstance(col, SYM):
                mode = col.mid()
                statistics[f"{col.txt}"] = int(mode) if type(mode) == float else mode
        return statistics


   
    def gate(self, budget0, budget, some):
        stats = []
        bests = []
        rows = random.sample(self.rows, len(self.rows)) 
    
        lite = rows[0:budget0]  
        dark = rows[budget0:]     

        for i in range(budget):
            best, rest = self.best_rest(lite, len(lite)**some)  
            todo, selected = self.split(best, rest, lite, dark)  
            
            stats.append(selected.mid())
            bests.append(best.rows[0])

        return stats, bests



    def stats_div(self, fun=None, ndivs=None):
        u = {}
        for col in self.cols.all:
            if isinstance(col, SYM):
                if col.txt == "origin":
                    u[col.txt] = round(col.div(), 2)
                else:
                    u[col.txt] = col.div()
            else:
                u[col.txt] = round(col.div(), 2)
        return u

    def mid_div(self):
        d2h_vals = [r.d2h(self) for r in self.rows]
        return [
            [self.stats(), round(np.mean(d2h_vals), 2)],
            [self.stats_div(), round(np.std(d2h_vals), 2)],
        ]

    def half(self, rows, sortp, before):
        the_half = min(len(rows) // 2, len(rows))
        some = random.sample(rows, the_half)
        a, b, C, evals = self.farapart(some, sortp, before)

        def d(row1, row2):
            return row1.dist(row2, self)

        def project(r):
            return (d(r, a) ** 2 + C**2 - d(r, b) ** 2) / (2 * C)

        rows_sorted = sorted(rows, key=project)
        mid_point = len(rows) // 2
        as_ = rows_sorted[:mid_point]
        bs = rows_sorted[mid_point:]
        return as_, bs, a, b, C, d(a, bs[0]), evals

    def split(self, best, rest, lite, dark):
        selected = DATA(self.cols.names, [])
        max_val = 0
        out = 1

        for i, row in enumerate(dark, 1):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            if b > r:
                selected.add(row)

            tmp = abs(b + r) / abs(b - r + 1e-300)
            if tmp > max_val:
                out, max_val = i, tmp

        return out, selected

    def farapart(self, rows, sortp, a=None, b=None, far=None, evals=0):
        far = int(len(rows) * 0.95) + 1
        evals = 1 if a is not None else 2

        a = a or random.choice(rows)

        sorted_neighbors = a.neighbors(self, rows)
        a = a or sorted_neighbors[0]
        b = sorted_neighbors[min(far, len(sorted_neighbors) - 1)]

        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a

        return a, b, a.dist(b, self), evals

    def far(the, data_new):
        print()
        print("Task 2: Get Far Working\n")
        target_distance = 0.95
        current_distance = 0
        attempts = 0

        while current_distance < target_distance and attempts < 200:
            a, b, C, _ = data_new.farapart(data_new.rows, sortp=True)
            current_distance = C
            attempts += 1
        if current_distance <= target_distance:
            print(f"far1: {a.cells}")
            print(f"far2: {b.cells}")
            print(f"distance: {current_distance}")
        else:
            print("No pair found")
        return current_distance, attempts

    def clone(self, rows=None):
        new = DATA()
        for row in rows or []:
            new.add(row)
        return new

    def tree(self, sortp):
        evals = 0

        def _tree(data, above=None):
            nonlocal evals
            node = NODE(data)

            if len(data.rows) > 2 * (len(self.rows) ** 0.5):
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = (
                    self.half(data.rows, sortp, above)
                )
                evals += evals1
                node.lefts = _tree(self.clone(lefts), node.left)
                node.rights = _tree(self.clone(rights), node.right)

            return node

        return _tree(self), evals

    def branch(self, stop=None, rest=None, _branch=None, evals=None):
        evals, rest = 1, []
        stop = stop or (2 * (len(self.rows) ** 0.5))

        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals, rest

            if len(data.rows) > stop:
                lefts, rights, left, _, _, _, _ = self.half(data.rows, True, above)
                evals += 1
                for row1 in rights:
                    rest.append(row1)

                return _branch(self.clone(lefts), left)
            else:
                return self.clone(data.rows), self.clone(rest), evals

        return _branch(self)

    def best_rest(self, rows, want):
        rows.sort(key=lambda a: a.d2h(self))
        best = DATA(self.cols.names)
        rest = DATA(self.cols.names)
        for i, row in enumerate(rows):
            if i < want:
                best.add(row)
            else:
                rest.add(row)
        return best, rest

    def clone(self, rows=None, newData=None):
        newData = DATA([self.cols.names])
        for row in rows or []:
            newData.add(row)
        return newData

    def any50(self, random_seed):
        random.seed(random_seed)
        rows = random.sample(self.rows, 50)
        return [rows[0].cells, round(rows[0].d2h(self), 2)]

    def best_100(self, random_seed):
        random.seed(random_seed)
        rows = random.sample(self.rows, len(self.rows))
        rows.sort(key=lambda row: row.d2h(self))
        return [rows[0].cells, round(rows[0].d2h(self), 2)]
    
