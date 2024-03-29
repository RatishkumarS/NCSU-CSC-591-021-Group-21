import sys
from config import CONFIG
from data import DATA
from tests import * 
from learn import *
import constants


def dist():
    data = DATA("auto93.csv")

    row1 = data.row[0]
    # print(row1.cells)

    rows = row1.neighbors(data)
    for i, row in enumerate(rows):
        if i % 30 == 0:
            print(i + 1, row.cells, row.dist(row1, data))


def cli():
    args = sys.argv[1:]
    temp = CONFIG()
    if len(args) > 0:
        for i in range(len(args)):
            if args[i] == "-k":
                constants.the["k"] = int(args[i + 1])
            if args[i] == "-m":
                constants.the["m"] = int(args[i + 1])
        if args[0] == "--help" or args[0] == "-h":
            print(temp.gethelp())
        if args[0] == "--file" or args[0] == "-f":
            file = str(args[1])
            bayes(file)
            dataobj = DATA(file)
        if args[0] == "--bayes4" or "-b4" in args:
            print("{:<20} {:<10} {:<10} {:<10}".format(file, "k", "m", "Accuracy"))
            for i in [0, 1, 2, 3]:
                constants.the["k"] = i
                for j in [0, 1, 2, 3]:
                    constants.the["m"] = j
                    file = str(args[1])
                    bayes(file)
                    dataobj = DATA(file)
        if args[0] == "--w5" or "-w5" in args:
            file=str(args[1])
            d=DATA(file)
            test_dist(d)
            test_far(file)
        if args[0] == "--dist" or args[0] == "-d":
            dist()
        if args[0] == "--test" or args[0] == "-t":
            if args[3] == "sym":
                print(test_sym())
            elif args[3] == "stats":
                fname = args[1].split("/")[-1]
                fstats = dataobj.stats()
                print(fstats)
            elif args[3] == "config":
                print(test_seed_cohen())


cli()
