import math


class SYM:
    def __init__(self, s=None, n=None):
        self.txt = s if s else " "
        self.at = n if n else 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            str_x = str(x)
            self.n += 1
            self.has[str_x] = 1 + (self.has[str_x] if str_x in self.has else 0)
            if self.has[str_x] > self.most:
                self.most, self.mode = self.has[str_x], x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for v in self.has.values():
            e += -v / self.n * math.log2(v / self.n)
        return e
