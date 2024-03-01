import csv
from row import ROW
from cols import COLS
from constants import *
from sym import SYM
import numpy as np
import random
import ast


class DATA:
    def __init__(self, src, fun=None):
        self.row = []
        self.cols = None
        if isinstance(src, str):
            with open(src, "r") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.add(row, fun)

    def add(self, t, fun, row=None):
        if isinstance(t, ROW):
            row = t.cells
        else:
            row = ROW(t)

        if self.cols:
            if fun:
                fun(self, row)
            self.row.append(self.cols.add(row))
        else:
            self.cols = COLS(t)

    def mid(self, cols, u):
        u = []
        for col in self.cols or self.cols.all:
            u.append(col.mid())
        return ROW(u)

    def div(self, cols, u):
        u = []
        for col in self.cols or self.cols.all:
            u.append(col.div())
        return ROW(u)

    def small(self, u):
        u = []
        for col in self.cols.all:
            u.append(col.small())
        return ROW(u)

    def stats(self, cols=None, fun=None, ndivs=None, u=None):
        u = {".N": len(self.row)}
        for i, j in zip(self.cols.names, self.cols.all):
            if i in ["Lbs-", "Acc+", "Mpg+"]:
                u[i] = round(j.mid(), 2)
        return u
    
    def farapart(self, rows, sortp=None, a=None, b=None):
        far = int(len(rows) * 0.95)
        evals = 1 if a else 2
        a = a or random.choice(rows).neighbors(self, rows)
        print(a)
        b = a.neighbors(self, rows)[far]
        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a
        return a, b, a.dist(b, self), evals

    def many(self, t, n):
        n = n or len(t)
        return [random.choice(t) for _ in range(n)]

    def half(self, rows, sortp, before):
        # print(self.the.Half)
        some = self.many(rows, min(256, len(rows)))
        a, b, C, evals = self.farapart(some, sortp, before)

        def dist(row1, row2):
            return row1.dist(row2, self)

        def project(r):
            return (dist(r, a) ** 2 + C**2 - dist(r, b) ** 2) / (2 * C)

        as_, bs = [], []
        for n, row in enumerate(self.util.keysort(rows, project)):
            if n <= (len(rows) // 2 - 1):
                as_.append(row)
            else:
                bs.append(row)

        return as_, bs, a, b, C, dist(a, bs[0]), evals

    def bins(self, stop=None):
        evals = 1
        rest = []
        if not stop:
            stop = 2 * (len(self.row)) ** 0.5

        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals
            if len(data.row) > stop:
                lefts, rights, left, _, _, _, _ = self.half(data.row, True, above)
                evals += 1
                rest.extend(rights)
                return _branch(data.clone(lefts), left)
            else:
                return self.clone(data.row), self.clone(rest), evals

        return _branch(self)
