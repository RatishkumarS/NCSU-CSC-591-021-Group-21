from hw.w8.src.Stats import NUM
import random
import sys
from config import CONFIG
from data import DATA
from test import *
from learn import *
import constants, re, time
from datetime import datetime
from statistics import mean ,stdev


def dist():
    data = DATA("auto93.csv")

    row1 = data.row[0]
    # print(row1.cells)

    rows = row1.neighbors(data)
    for i, row in enumerate(rows):
        if i % 30 == 0:
            print(i + 1, row.cells, row.dist(row1, data))

def set_random_seed():
        seed = int(re.sub(r'[^0-9]', '', str(time.time())[-7:]))
        return seed

def display_smo9():
        data = DATA("auto93.csv")
        
        data_new = DATA("auto93.csv")
        full_mid, full_div = data_new.mid_div()

        smo_output = []
        any50_output = []

        budget0, budget, some = 4, 10, 0.5
        for i in range(20):
            random_seed = set_random_seed()
            d = DATA("auto93.csv") 
            ign1, ign2, line = d.gate(random_seed, budget0, budget, some)
            smo_output.append(line)
            any50_output.append(d.any50(random_seed))

        best = d.best_100(random_seed)
    
        print("date : {} \nfile : {} \nrepeat : {} \nseed : {} \nrows : {} \ncols : {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"auto93.csv","20","32400",len(data_new.rows), len(data_new.rows[0].cells)))
        print("names : \t{}\t\t{}".format(d.cols.names,"D2h-"))
        print("mid : \t\t{}\t\t\t\t{}".format(list(full_mid[0].values())[1:],full_mid[1]))
        print("div : \t\t{}\t\t\t\t\t{}".format(list(full_div[0].values())[1:],full_div[1]))
        print("#")
        smo_output = sorted(smo_output, key=lambda x: x[1])
        for op in smo_output:
            print("smo9\t\t{}\t\t\t\t{}".format(op[0],op[1]))
        print("#")
        any50_output = sorted(any50_output, key=lambda x: x[1])
        for op in any50_output:
            print("any50\t\t{}\t\t\t\t{}".format(op[0],op[1]))
        print("#")
        print("100%\t\t{}\t\t\t\t{}".format(best[0],best[1]))
def smo_stats():
    data =DATA("auto93.csv")
    print("date : {} \nfile : {} \nrepeat : {} \nseed : {} ".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"auto93.csv","20","32400"))
    r=data.rows
    r.sort(key=lambda x: x.d2h(data))
    ceil=rnd(r[0].d2h(data))
    bonr9=[]
    rand358=[]
    rand20=[]
    bonr20=[]
    rand15=[]
    bonr15=[]
    rand9=[]
    for i in range(20):
        bonr9.append(bonr_col(9))
        rand9.append(rand_col(9))
        bonr15.append(bonr_col(15))
        rand15.append(rand_col(20))
        bonr20.append(bonr_col(20))
        rand20.append(rand_col(20))
        rand358.append(rand_col(358))
    all_std=all_std_rows(data.rows,data)
    stddev=stdev(all_std)
    tiny=rnd(0.35*stddev)
    print("best:{} \ntiny:{}".format(ceil,tiny))
    print("base bonr9 rand9 bonr15 rand15 bonr20 rand20 rand358")
    print("Report8")
    NUM.eg0([
        NUM(bonr9,"bonr9"),
        NUM(rand9,"rand9"),
        NUM(bonr15,"bonr15"),
        NUM(rand15,"rand15"),
        NUM(bonr20,"bonr20"),
        NUM(rand20,"rand20"),
        NUM(rand358,"rand358"),
        NUM(all_std,"base")
    ])
def bonr_col(n):
    data=DATA("auto93.csv")
    stats,bests,x=data.gate(32400,4,n-4,0.5)
    stat,best=stats[-1],bests[-1]
    return rnd(best.d2h(data))
def rand_col(n):
    data=DATA("auto93.csv")
    r=random.sample(data.rows,n)
    r.sort(key=lambda x:x.d2h(data))
    return rnd(r[0].d2h(data))
def all_std_rows(rowss,data):
    all_d2h=[]
    for rows in rowss:
        all_d2h.append(rows.d2h(data))
    return all_d2h

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
        if args[0] == "--dist" or args[0] == "-d":
            dist()
        if args[0] == "--smo9":
            display_smo9()
        if args[0] == "--w8Task2":
            smo_stats()
        if args[0] == "--test" or args[0] == "-t":
            if args[3] == "stats":
                fname = args[1].split("/")[-1]
                fstats = dataobj.stats()
                print(fstats)
cli()
