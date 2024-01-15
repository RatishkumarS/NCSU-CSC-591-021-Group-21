from num import NUM
from sym import SYM
import re

class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = [], [], []
        self.klass, self.col = None, None
        for at, txt in row['cells'].items():
            print(at)
            print(txt)
            col = NUM(str(txt), at) if str(txt)[0].isalpha() and str(txt)[0].isupper() else SYM(str(txt), at)
            self.all.append(col)
            if not re.search(r"X$", str(txt)):
                if re.search(r"!$", str(txt)):
                    self.klass = col
                (self.y if re.search(r"[!+−]$", str(txt)) else self.x).append(col)
        self.names = row['cells']

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols:
                col.add(row.cells[col.at])
        
        return row
