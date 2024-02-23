import ast


class CONFIG:
    def __init__(self):
        self.the = {"dump": False, "go": None, "seed": 937162211, "cohen": 0.35}

        self.help = """USAGE:   python main.py [OPTIONS] [-g ACTION]
            OPTIONS:
            -d  --dump  on crash, dump stack = false
            -g  --go    start-up action      = data
            -h  --help  show help            = false
            -s  --seed  random number seed   = 31210
            −f  −−file  csv data file name   = ../data/diabetes.csv
            −c  −−cohen small effect size    = .35
        """

        self.egs = {}

        self.seed = 31210

    def gethelp(self):
        return self.help

    def setthe(self, att, value):
        if att == "seed":
            self.the[att] = int(value)
        elif att == "cohen":
            self.the[att] = float(value)
def coerce(s1):
        try:
            return ast.literal_eval(s1)
        except:
            return s1.strip()
        if s1 == "nil":
            return None
        elif s1 == 'true':
            return True
        elif s1 == 'false':
            return False
        elif s1.isdigit():
            return int(s1)
        elif '.' in s1 and s1.replace('.','').isdigit():
            return float(s1)
        else:
            return s1
    