import math
import ast


class NUM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.low = 1E30
        self.heaven = 0 if (s or "").endswith("-") else 1

    def add(self, x, d=0):
        if x != "?":
            # x = ast.literal_eval(x)
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.low = min(x, self.low)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5

    def small(self):
        pass

    def norm(self, x):
        # print(type(x), "->",x)
        return x if x == "?" else (x - self.low) / (self.hi - self.low + 1E-30)

    def like(self, x, _):
        mu, sd = self.mid(), (self.div() + 1e-30)
        nom = math.exp(-0.5 * ((x - mu) ** 2) / (sd**2))
        denom = sd * 2.5 + 1e-30
        print(nom / denom)
        return nom / denom

    def dist(self, x, y):
        if x == "?" and y == "?":
            return 1
        x, y = self.norm(x), self.norm(y)
        if x == "?":
            x = 1 if y < 0.5 else 0
        if y == "?":
            y = 1 if x < 0.5 else 0
        return abs(x - y)
