from num import NUM
from sym import SYM
import re
from row import ROW


class COLS:
    def __init__(self, row):
        
        x, y, all_cols = {}, {}, []
        klass, col = None, None

        for at, txt in enumerate(row):
            col = (SYM if txt.startswith("A-Z") else NUM)(txt, at)
            all_cols.append(col)

            if not txt.endswith("X"):
                if txt.endswith("!"):
                    klass = col

                (y if txt.endswith("[!+−]") else x)[at] = col

        self.x = x
        self.y = y
        self.all = all_cols
        self.klass = klass
        self.names = row


    def print_cols(self):
        for col in self.all:
            print(col)

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols.values():
                col.add(row.cells[col.at])
        return row
