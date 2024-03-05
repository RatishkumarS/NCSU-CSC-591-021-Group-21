import math
from constants import *


class ROW:
    def __init__(self, t):
        self.cells = t

    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + the["k"]) / (n + the["k"] * nHypotheses)
        out = math.log(prior) if prior != 0 else float("-inf")

        for col in data.cols.x:
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out = out + (math.log(inc) if inc != 0 else float("-inf"))

        return math.exp(1) ** out

    def likes(self, datas):
        n, nHypotheses = 0, 0
        most, out = None, None

        for k, data in datas.items():
            n += len(data.row)
            nHypotheses += 1

        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, k

        return out, most
    
    def neighbors(self, data, rows=None):
        return self.keysort(rows or data.rows, lambda row: self.dist(row, data))

    def dist(self, other, data, d=0, n=0, p=None):
        d, n, p = 0, 0, 2  # Assuming the.p is defined in the scope
        # print("dist->",other.cells)
        for col in data.cols.x:
            n += 1
            d += math.pow(col.dist(self.cells[col.at], other.cells[col.at]), p)

        return (d / n) ** (1 / p)
    
    def keysort(self, t, fun):
        u = [{'x': x, 'y': fun(x)} for x in t]
        u.sort(key=lambda a: a['y'])
        v = [xy['x'] for xy in u]
        return v
    
    def d2h(self, data):
        d, n, p = 0, 0, 2
        for col in data.cols.y:
            n += 1
            d += abs(col.heaven - col.norm(self.cells[col.at])) ** p
        return math.sqrt(d) / math.sqrt(n)
