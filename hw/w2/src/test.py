from sym import SYM
from num import NUM
from config import CONFIG


def test_stat(fstats):
    expect_stat = {".N": 398, "Acc+": 15.57, "Lbs-": 2970.42, "Mpg+": 23.84}
    assert fstats== expect_stat
    return 1
    

def test_help():
    obj=CONFIG()
    print(obj.gethelp())

def test_teardown_reset_config():
    obj = CONFIG()
    obj.setthe("seed",31210)
    obj.setthe("cohen",0.35)
    return obj.the['seed']==31210 and obj.the['cohen']==0.35
