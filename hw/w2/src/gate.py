import sys
from config import CONFIG
from data import DATA
from helpers import *
from hw.w2.src.test import test_stat,test_help,test_teardown_reset_config

def cli():
    args = sys.argv[1:]
    temp = CONFIG()
    if args[0] == '--help' or args[0] == "-h":
        print(test_help())
    elif args[0] == '--file' or args[0]=="-f":
        file = str(args[1])
        dataobj = DATA(file)
        if args[2] == "--test" or args[2]=="-t":
            if args[3] == "stats":
                fstats = dataobj.stats()
                if (test_stat(fstats)==1):
                    print(fstats)
                    print('# ✅ PASS ')
                else:
                    print('# ❌ FAIL ')
            elif args[3] == "reset_config":
                print(test_teardown_reset_config())
    else:
        attr = args[0][2:]
        val = args[1]
        temp.the_setter(attr,val)

cli()