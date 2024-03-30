import sys
from config import CONFIG
from data import DATA
from test import *
from learn import *
import constants, re, time
from datetime import datetime
import random, math
from range import RANGE
from Rules import Rules
from data import *


def o(t, n=None, u=None):
    if isinstance(t, (int, float)):
        return str(round(t, n))
    if not isinstance(t, dict):
        return str(t)

    u = []
    for k, v in t.items():
        if str(k)[0] != "_":
            if len(t) > 0:
                u.append(o(v, n))
            else:
                u.append(f"%s: %s", o(k, n), o(v, n))

    return "{" + ", ".join(u) + "}"


def dist():
    data = DATA("auto93.csv")

    # row1 = data.rows[0]
    # # print(row1.cells)

    # rows = row1.neighbors(data)
    # for i, row in enumerate(rows):
    #     if i % 30 == 0:
    #         print(i + 1, row.cells, row.dist(row1, data))

    data_new = DATA("auto93.csv")
    # DATA.far(the, data_new)

    # t, evals = data_new.tree(True)
    # t.show()
    # print("evals: ", evals)

    # print("Task 2: Optimization - Single Descent\n")
    # best, rest, evals = data_new.branch()
    # print("centroid of output cluster: ")
    # print(o(best.mid().cells), o(rest.mid().cells))
    # print("evals: ", evals)

    print("Task 3: Doubletap\n")
    best1, rest, evals1 = data_new.branch(32)
    best2, _, evals2 = best1.branch(4)
    print("Median and Best: ")
    print(o(best2.mid().cells), o(rest.mid().cells))
    print("evals: ", evals1 + evals2)


def set_random_seed():
    seed = int(re.sub(r"[^0-9]", "", str(time.time())[-7:]))
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

    print(
        "date : {} \nfile : {} \nrepeat : {} \nseed : {} \nrows : {} \ncols : {}".format(
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "auto93.csv",
            "20",
            "32400",
            len(data_new.rows),
            len(data_new.rows[0].cells),
        )
    )
    print("names : \t{}\t\t{}".format(d.cols.names, "D2h-"))
    print("mid : \t\t{}\t\t\t\t{}".format(list(full_mid[0].values())[1:], full_mid[1]))
    print(
        "div : \t\t{}\t\t\t\t\t{}".format(list(full_div[0].values())[1:], full_div[1])
    )
    print("#")
    smo_output = sorted(smo_output, key=lambda x: x[1])
    for op in smo_output:
        print("smo9\t\t{}\t\t\t\t{}".format(op[0], op[1]))
    print("#")
    any50_output = sorted(any50_output, key=lambda x: x[1])
    for op in any50_output:
        print("any50\t\t{}\t\t\t\t{}".format(op[0], op[1]))
    print("#")
    print("100%\t\t{}\t\t\t\t{}".format(best[0], best[1]))


def _ranges1(col, rowss):
    out, nrows = {}, 0
    for y, rows in rowss.items():
        nrows += len(rows)
        for row in list(rows):
            x = row.cells[col.at]
            if x != "?":
                bin = col.bin(x)
                if bin not in out:
                    out[bin] = RANGE(col.at, col.txt, x)
                out[bin].add(x, y)
    out = list(out.values())
    out.sort(key=lambda r: r.x["lo"])
    return out if hasattr(col, "has") else _mergeds(out, nrows / 16)
def _mergeds(ranges, tooFew):
        t = []
        i = 1
        while i <= len(ranges):
            a = ranges[i - 1]
            if i < len(ranges):
                both = a.merged(ranges[i], tooFew)
                if both:
                    a = both
                    i += 1
            t.append(a)
            i += 1
        if len(t) < len(ranges):
            return _mergeds(t, tooFew)
        for i in range(1, len(t)):
            t[i].x["lo"] = t[i - 1].x["hi"]
        t[0].x["lo"] = -math.inf
        t[-1].x["hi"] = math.inf
        return t

def _ranges(cols, rowss):
    t = []
    for col in cols:
        for range in _ranges1(col, rowss):
            t.append(range)
    return t



def bins():
    d = DATA("auto93.csv")
    best, rest, _ = d.branch()
    LIKE = best.rows
    HATE = list(random.sample(rest.rows, min(3 * len(LIKE), len(rest.rows))))

    # print(type(LIKE))
    # print(type(HATE))

    def score(range_):
        return range_.score("LIKE", len(LIKE), len(HATE))

    print()
    print("PART - 1")
    t = []
    for col in list(d.cols.x):
        print("")
        for range_ in _ranges1(col, {"LIKE": LIKE, "HATE": HATE}):
            temp_x = {"hi": range_.x["hi"], "lo": range_.x["lo"]}
            temp_y = {}
            if "HATE" in range_.y:
                temp_y["HATE"] = range_.y["HATE"]
            if "LIKE" in range_.y:
                temp_y["LIKE"] = range_.y["LIKE"]
            d = {
                "at": (range_.at) + 1,
                "scored": range_.scored,
                "txt": range_.txt,
                "x": temp_x,
                "y": temp_y,
            }
            print(d)
            t.append(range_)
    t.sort(key=lambda a: score(a), reverse=True)
    max_score = score(t[0])
    print("\n\nPART - 2")
    print("\n#scores:\n")
    for v in t[: int(10)]:
        if score(v) > max_score * 0.1:
            temp_x = {"hi": v.x["hi"], "lo": v.x["lo"]}
            temp_y = {}
            if "HATE" in v.y:
                temp_y["HATE"] = v.y["HATE"]
            if "LIKE" in v.y:
                temp_y["LIKE"] = v.y["LIKE"]
            d_v = {
                "at": (v.at) + 1,
                "scored": v.scored,
                "txt": v.txt,
                "x": temp_x,
                "y": temp_y,
            }
            print("{:.2f}".format(round(score(v), 2)), d_v)
    print(
        {
            "HATE": len(HATE),
            "LIKE": len(LIKE),
        }
    )
def eg_bins():
    d = DATA("auto93.csv")

    bests, rest,ed1= d.branch(the['d'])

    LIKE = bests.rows
    HATE = random.sample(rest.rows, 3 * len(LIKE))
    rowss = {"LIKE": LIKE, "HATE": HATE}

    rules = Rules(_ranges(d.cols.x, rowss), "LIKE", rowss)

    print("score\t\t\t\t\t\t", "mid selected\t\t\t\t\t\t\t\t\t\t\t", "rules")
    print("=================================================================================================================================================================================================")
    for rule in rules.sorted:
        result = d.clone(rule.selects(rest.rows))
        if len(result.rows) > 0:
            result.rows.sort(key=lambda x: x.d2h(d))
            print(rnd(rule.scored), "\t","\t\t", o(result.mid().cells), "\t", rule.show())

def rnd(n, ndecs = 2):
    if type(n) != int and type(n) != float:
        return n
    if math.floor(n) == n:
        return n
    mult = 10 ** ndecs
    return math.floor(n * mult + 0.5) / mult


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
        if args[0] == "--bins":
            bins()
        if args[0] == "--rules":
            eg_bins()
        if args[0] == "--test" or args[0] == "-t":
            if args[3] == "stats":
                fname = args[1].split("/")[-1]
                fstats = dataobj.stats()
                print(fstats)


cli()
