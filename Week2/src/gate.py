from helpers import *
from test import *

def run(k):
    b4 = copy.deepcopy(the)
    random.seed(the['seed'])
    if the['help'] == True:
        print(help)
    oops = egs[k]()
    if oops == False:
        print('# ❌ FAIL ', k)
    else:
        print('# ✅ PASS ', k)
    for k,v in b4.items():
        the[k] = v
    return oops

the = settings(help)
egs['help'] = test_try
egs['stats'] = test_stats
run(cli(the)['todo'])