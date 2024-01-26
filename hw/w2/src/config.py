class CONFIG:
    def __init__(self):
        self.the = {}
        self.b4 = {}
        self.egs = {}

        self.help= """USAGE:   python main.py [OPTIONS] [-g ACTION]
            OPTIONS:
            -c --cohen    small effect size               = .35
            -f --file     csv data file name              = ../data/diabetes.csv
        @@ -11,4 +11,6 @@
            -m --m        low attribute frequency kludge  = 2
            -s --seed     random number seed              = 31210
            -t --todo     start up action                 = help
            """
    def the_setter(self,att,value):
        if att=="seed":
            self.the[att] = int(value)
        elif att=="cohen":
            self.the[att] = float(value)
            
    def gethelp(self):
        return self.help
    
    