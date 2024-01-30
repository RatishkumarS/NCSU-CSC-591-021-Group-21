import csv
from row import ROW
from cols import COLS
import random

class DATA:
    def __init__(self, src, fun=None):
        self.row = []
        self.cols = None
        if isinstance(src,str):
            with open(src, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.add(row,fun)

    def add(self,t,fun,row=None):
        if isinstance(t,ROW):
            row = t.cells
        else:
            row = ROW(t)

        if self.cols:
            if fun:
                fun(self,row)
            self.row.append(self.cols.add(row))
        else:
            self.cols = COLS(t)

    def mid(self,cols,u):
        u = []
        for col in (self.cols or self.cols.all):
            u.append(col.mid())
        return ROW(u)
    
    def div(self,cols,u):
        u = []
        for col in (self.cols or self.cols.all):
            u.append(col.div())
        return ROW(u)
    
    def small(self,u):
        u = []
        for col in self.cols.all:
            u.append(col.small())
        return ROW(u)
    
    def stats(self, cols=None, fun=None, ndivs=None, u=None):
        u = {".N":len(self.row)}
        for i,j in zip(self.cols.names,self.cols.all):
            if i in ['Lbs-','Acc+','Mpg+']:
                u[i] = round(j.mid(),2)
        return u
    
    
    
    def gate(self, budget0, budget, some):
        rows, lite, dark = None, None, None
        stats, bests = {}, {}
        rows = random.shuffle(self.row)
        lite = rows[1:budget0]
        dark = rows[budget0+1:]
        for i in range(1, budget + 1):
            best, rest = self.bestRest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark)
            stats[i] = selected.mid()
            bests[i] = best.rows[0]
            item = dark.pop(todo)
            lite.append(item)
        return stats,bests
    
    def best_rest(data, want):
        data.rows.sort(key=lambda row: row.d2h())
        best, rest = [data.cols.names], [data.cols.names]
        
        for i, row in enumerate(data.rows, 1):
            if i <= want:
                best.append(row)
            else:
                rest.append(row)

        return DATA(best), DATA(rest)