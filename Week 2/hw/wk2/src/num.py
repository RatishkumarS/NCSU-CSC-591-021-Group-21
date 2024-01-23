import math
import ast

class NUM:
    def __init__(self,s=None,n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n=0
        self.mu=0
        self.m2=0
        self.hi = -float('inf')
        self.low = float('inf')
        self.heaven = 0 if (s or "").endswith("-") else 1

    def add(self,x,d=0):
        if x!="?":
            x = ast.literal_eval(x)
            self.n+=1
            d = x - self.mu
            self.mu += d/self.n
            self.m2 += d*(x-self.mu)
            self.low = min(x,self.low)
            self.hi = max(x,self.hi)

    def mid(self):
        return self.mu
    
    def div(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1))**0.5
    
    def small(self):
        pass

    def norm(self,x):
        pass

