import ast
import fileinput
import re
from cols import COLS
from row import ROW


class DATA:
    def __init__(self, src):
        self.rows = []
        self.cols = None

        if isinstance(src, str):
            for x in self.csv(src):
                # print(x)
                self.add(x)
        else:
            for x in src or []:
                self.add(x)

    def print_rows(self):
        for row in self.rows:
            print(row.cells)

    def print_cols(self):
        if self.cols:
            self.cols.print_cols()
        else:
            print("No columns available.")

    def mid(self, cols=None):
        u = []
        for col in cols or (self.cols.all if self.cols else []):
            u.append(col.mid())

        return ROW(u)

    def coerce(self, s):
        try:
            return ast.literal_eval(s)
        except Exception:
            return s

    def csv(self, file="-"):
        lines = []
        with fileinput.FileInput(None if file == "-" else file) as src:
            for line in src:
                line = re.sub(r'([\n\t\r"\' ]|#.*)', "", line)
                if line:
                    yield [self.coerce(x) for x in line.split(",")]
                    lines.append(line)

        return lines

    def add(self, t, fun=None, row=None):
        row = t["cells"] if "cells" in t else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            # print(row.cells)
            # print("Inside else of add - data")
            self.cols = COLS(row)


# data_instance = DATA("auto93.csv")
# result_all_columns = data_instance.mid()
# print("Output for all columns:")
# print(result_all_columns.cells)
