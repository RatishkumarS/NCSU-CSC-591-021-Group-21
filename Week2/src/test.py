from helpers import *
from data import DATA


def test_stats():
    datas = DATA(the["file"])
    expect_stat = {".N": 398, "Acc+": 15.57, "Lbs-": 2970.42, "Mpg+": 23.84}
    assert datas.stats() == expect_stat
    print(datas.stats())


def test_try():
    return ("\n", help)
