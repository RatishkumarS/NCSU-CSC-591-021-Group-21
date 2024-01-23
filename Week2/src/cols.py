from num import NUM
from sym import SYM
import re


class COLS:
    def __init__(self, row):
        # print(row.cells)
        self.x, self.y, self.all = [], [], []
        self.klass, self.col = None, None
        for at, txt in enumerate(row.cells):
            # print(at)
            # print(txt)
            col = (
                NUM(txt, at) if txt[0].isalpha() and txt[0].isupper() else SYM(txt, at)
            )
            # print(col)
            # print(col.txt)
            self.all.append(col)
            if not re.search(r"X$", txt):
                if re.search(r"!$", txt):
                    self.klass = col
                (self.y if re.search(r"[!+−]$", txt) or "-" else self.x).append(col)
        self.names = row.cells
        # print(self.names)
        # print(self.x)

    def print_cols(self):
        for col in self.all:
            print(col)

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols:
                col.add(row.cells[col.at])

        return row
