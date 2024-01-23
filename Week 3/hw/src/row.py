import math

class ROW:
    def __init__(self, t):
        self.cells = t
        self.k = 1

    @classmethod
    def new(cls, t):
        return cls(t)
    
    def like(self, data, n, nHypotheses):
        prior = (len(data.row) + self.k) / (n + self.k * nHypotheses)
        out = math.log(prior)

        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                if inc > 0:
                    out += math.log2(inc)

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