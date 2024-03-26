import math


class NUM:
    def __init__(self, s=" ", n=0):
        self.txt = s
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1e30
        self.lo = 1e30
        self.heaven = 0 if (s or "").endswith("-") else 1

    def add(self, x):
        if x != "?" and isinstance(x, (int, float)):
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1e-30)

    def like(self, x, prior):
        mu, sd = self.mid(), (self.div() + 1e-30)
        nom = math.exp(-0.5 * ((x - mu) ** 2) / (sd**2))
        denom = sd * 2.5 + 1e-30
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

    # Function bin
    def bin(self, x):
        tmp = (self.hi - self.lo)/(15)
        return 1 if self.hi == self.lo else int(x/tmp+0.5)*tmp