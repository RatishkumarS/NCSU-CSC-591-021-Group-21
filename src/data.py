import csv
from helpers import *
from row import ROW
from cols import COLS


class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None
        self.adds(src, fun)

    def add(self,t):
        if self.cols:
            t=ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=COLS(t)

    def adds(self,src,fun):
        if isinstance(src,str):
            csv(src,self.add)
        else:
            for record in src():
                self.add(record)

    def stats(self, cols=None, fun="mid", ndivs=2):
        u = {".N": len(self.rows)}
        cols = cols or self.cols.y
        for col in cols:
            col_name = col.txt
            col_function = getattr(col, fun, col.mid)  # Using getattr to get the function dynamically
            col_value = col_function()
            u[col_name] = round(col_value, ndivs) if ndivs is not None else col_value
        return u

# data_instance = DATA("auto93.csv")
# print("Output for all columns:")
# print(result_all_columns.cells)
