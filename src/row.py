import math


class ROW:
    def __init__(self, t):
        self.cells = t
        self.k = 1

    def likes(self, datas):
        n, nHypotheses = 0
        most, out = None, 0
        for k, data in enumerate(datas):
            n = n + len(data)
            nHypotheses = nHypotheses + 1
        for k, data in enumerate(datas):
            temp = self.like(data, n, nHypotheses)
            if most is None or temp > most:
                most, out = temp, k
        return out, most

    def like(self, data, n, nHypotheses):
        prior = (len(data) + self.k) / (n + self.k * nHypotheses)
        out = math.log(prior)
        for col in cols:
            v = self.cells[col]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)

        return math.exp(1) ** out
