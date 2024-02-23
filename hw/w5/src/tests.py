import math
import random
from sym import SYM
from config import CONFIG
from config import *
from data import DATA


def test_sym():
    obj = SYM()
    for x in [1, 1, 1, 2, 2, 2, 2, 3, 4]:
        obj.add(x)

    return obj.mid() == 2 and round(obj.div(), 2) == 1.75


def test_stat(name, vals):
    if name == "auto93.csv":
        print(
            vals[".N"] == 398
            and vals["Lbs-"] == 8.38
            and vals["Acc+"] == 5.94
            and vals["Mpg+"] == 1.77
        )


def test_seed_cohen():
    obj = CONFIG()
    obj.setthe("seed", 12345)
    obj.setthe("cohen", 0.67)
    return obj.the["seed"] == 12345 and obj.the["cohen"] == 0.67

def test_dist(d):
    r1=d.row[0]
    rows=r1.neighbors(d)
    for i,row in enumerate(rows):
        if i%30==0:
            print(i+1,o(row.cells),rnd(row.dist(r1,d)))
def test_far(file):
    print("======================Task2=========================")
    d = DATA(file)
    a, b, C,evals= d.farapart(d.row)
    print("Far 1:", a.cells)
    print("Far 2:", b.cells)
    print("distance = ",C)

def o(t, n=None):
        if isinstance(t, (int, float)):
            return str(random.randint(0, t))
        if not isinstance(t, dict):
            return str(t)
        return "{" + ", ".join(map(str,t)) + "}"

def rnd(n, ndecs=None):
    if not isinstance(n, (int, float)):
        return n
    if math.floor(n) == n:
        return n
    mult = 10 ** (ndecs or 2)
    return math.floor(n * mult + 0.5) / mult





