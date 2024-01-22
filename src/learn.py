from data import DATA
from config import the


def learn(data, row, my):
    my['n'] += 1
    print(row.cells)
    kl = row.cells[data.cols.klass.at]
    if my['n'] > 10:
        my['tries'] += 1
        my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0
    print(data.cols.names)
    if kl not in data:
        my['datas'][kl] = DATA(data.cols.names)
    my['datas'][kl].add(row['cells'])


def bayes():
    wme = {"acc": 0, "datas": {}, "tries": 0, "n": 0}
    llearn = lambda data, t: learn(data, t, wme)
    DATA(the['file'], llearn)
    print("Accuracy :", (wme['acc'] / wme['tries']) * 100)
