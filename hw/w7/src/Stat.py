import sys, random

class Num:
  def __init__(self,lst=[],txt="",rank=0):
    self.has,self.check = [],False
    self.txt, self.rank = txt,0
    self.n, self.sd, self.m2,self.mu, self.lo, self.hi = 0,0,0,0, sys.maxsize, -sys.maxsize
    for t in lst:
      self.push(t)
  
  def push(self,t):
    self.has += [t]
    self.check=False
    self.lo = min(t,self.lo)
    self.hi = max(t,self.hi)
    self.n += 1
    delta = t - self.mu
    self.mu += delta / self.n
    self.m2 += delta * (t -  self.mu)
    self.sd = 0 if self.n < 2 else (self.m2 / (self.n - 1))**.5


  def status_check(self):
    if not self.check: 
      self.has = sorted(self.has)
    self.check=True
    return self
  
  def mid(self): 
    has=self.status_check().has
    return has[len(has)//2]

  def bar(self, num, fmt="%8.3f", word="%10s", width=50):
    out  = [' '] * width
    pos = lambda x: int(width * (x - self.lo) / (self.hi - self.lo + 1E-30))
    [a, b, c, d, e]  = [num.has[int(len(num.has)*x)] for x in [0.1,0.3,0.5,0.7,0.9]]
    [na,nb,nc,nd,ne] = [pos(x) for x in [a,b,c,d,e]]
    for i in range(na,nb): out[i] = "-"
    # for i in range(nd,ne): out[i] = "-"
    out[width//2] = "|"
    out[nc] = "*"
    return ', '.join(["%2d" % num.rank, word % num.txt, fmt%c, fmt%(d-b),
                      ''.join(out), fmt%self.lo,fmt%self.hi])

def different(x,y):
  "non-parametric effect size and significance test"
  return _cliffsDelta(x,y) and _bootstrap(x,y)

def _cliffsDelta(x, y, effectSize=0.2):
  """non-parametric effect size. threshold is border between small=.11 and medium=.28 
     from Table1 of  https://doi.org/10.3102/10769986025002101"""
  #if len(x) > 10*len(y) : return cliffsDelta(random.choices(x,10*len(y)),y)
  #if len(y) > 10*len(x) : return cliffsDelta(x, random.choices(y,10*len(x)))
  n,lt,gt = 0,0,0
  for x1 in x:
    for y1 in y:
      n += 1
      if x1 > y1: gt += 1
      if x1 < y1: lt += 1
  return abs(lt - gt)/n  > effectSize # true if different

def _bootstrap(y0,z0,confidence=.05,Experiments=512,):
  """non-parametric significance test From Introduction to Bootstrap, 
     Efron and Tibshirani, 1993, chapter 20. https://doi.org/10.1201/9780429246593"""
  obs = lambda x,y: abs(x.mu-y.mu) / ((x.sd**2/x.n + y.sd**2/y.n)**.5 + 1E-30)
  x, y, z = Num(y0+z0), Num(y0), Num(z0)
  d = obs(y,z)
  yhat = [y1 - y.mu + x.mu for y1 in y0]
  zhat = [z1 - z.mu + x.mu for z1 in z0]
  n      = 0
  for _ in range(Experiments):
    ynum = Num(random.choices(yhat,k=len(yhat)))
    znum = Num(random.choices(zhat,k=len(zhat)))
    if obs(ynum, znum) > d:
      n += 1
  return n / Experiments < confidence 


def sk(nums):
  def sk1(nums, rank,lvl=1):
    all = lambda lst:  [x for num in lst for x in num.has]
    b4, cut = Num(all(nums)) ,None
    max =  -1
    for i in range(1,len(nums)):  
      lhs = Num(all(nums[:i])); 
      rhs = Num(all(nums[i:])); 
      tmp = (lhs.n*abs(lhs.mid() - b4.mid()) + rhs.n*abs(rhs.mid() - b4.mid()))/b4.n 
      if tmp > max:
         max,cut = tmp,i 
    if cut and different( all(nums[:cut]), all(nums[cut:])): 
      rank = sk1(nums[:cut], rank, lvl+1) + 1
      rank = sk1(nums[cut:], rank, lvl+1)
    else:
      for num in nums: num.rank = rank
    return rank
  #------------ 
  nums = sorted(nums, key=lambda num:num.mid())
  sk1(nums,0)
  return nums

def egSlurp():
  eg0(slurp("stats.txt"))

def eg0(nums):
  total= Num([x for num in nums for x in num.has])
  final = None
  for num in sk(nums):
    if num.rank != final: print("#")
    final=num.rank
    print(total.bar(num,width=40,word="%20s", fmt="%5.2f"))

def of(s):
    try: return float(s)
    except ValueError: return s

def slurp(file):
  nums,lst,last= [],[],None
  with open(file) as fp: 
    for word in [of(x) for s in fp.readlines() for x in s.split()]:
      if isinstance(word,float):
        lst += [word]
      else:
        if len(lst)>0: nums += [NUM(lst,last)]
        lst,last =[],word
  if len(lst)>0: nums += [NUM(lst,last)]
  return nums