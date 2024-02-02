from data import DATA
import sys
from constants import *


def learn(data, row, my):
        my['n'] += 1
        kl = row.cells[data.cols.klass.at]
        if my['n'] > 10:
            my['tries'] += 1
            my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0
        if kl not in my["datas"]:  
            my['datas'][kl] = DATA(data.cols.names)
        my['datas'][kl].add(row.cells, None)


def bayes(file):
        wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
        llearn = lambda data, t: learn(data, t, wme)
        DATA(file, llearn)
        print("Accuracy for ",file," : ", (wme['acc']/wme['tries'])*100)

def bayes(file):
    wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
    llearn = lambda data, t: learn(data, t, wme)
    DATA(file, llearn)
    accuracy_percentage = (wme['acc'] / wme['tries']) * 100
    print("{:<20} {:<10} {:<10} {:<10}".format(file, the['k'], the['m'], "{:.2f}%".format(accuracy_percentage)))

# Example usage:
# bayes("example_file.txt", 5, 10)
