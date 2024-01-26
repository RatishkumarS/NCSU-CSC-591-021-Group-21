import math


class NUM:
    def __init__(self, s, n):
        # txt - Column Name
        self.txt = s if s else " "
        # at - Column Number
        self.at = n if n else 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = float("-inf")
        self.lo = float("inf")

    def add(self, x):
        if x != "?":
            self.n = self.n + 1
            d = x - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        if self.n < 2:
            return 0
        else:
            return math.pow((self.m2 / (self.n - 1)), 0.5)