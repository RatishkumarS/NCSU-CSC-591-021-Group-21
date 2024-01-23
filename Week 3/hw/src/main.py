import sys
from config import CONFIG
from data import DATA
from test import *

def cli():
    args = sys.argv[1:]
    temp = CONFIG()
    if args[0] == '--help' or args[0] == "-h":
        print(temp.gethelp())
    elif args[0] == '--file' or args[0]=="-f":
        file = str(args[1])
        dataobj = DATA(file)
        if args[2] == "--test" or args[2]=="-t":
            if args[3] == "sym":
                print(test_sym())
            elif args[3] == "stats":
                fname = args[1].split("/")[-1]
                fstats = dataobj.stats()
                print(fstats)
            elif args[3] == "config":
                print(test_seed_cohen())
        
    else:
        attr = args[0][2:]
        val = args[1]
        temp.setthe(attr,val)

cli()