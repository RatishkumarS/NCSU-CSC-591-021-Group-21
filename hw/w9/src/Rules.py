from Rule import Rule
from constants import the

class Rules:
    def __init__(self, ranges, goal, rowss):
        self.sorted = []
        self.goal = goal
        self.rowss = rowss
        self.LIKE = 0
        self.HATE = 0
        self.likeHate()
        for range in ranges:
            range.scored = self.score(range.y)
        self.sorted = self.top(self.trys(self.top(ranges)))

    def score(self, t):

        return score(t, self.goal, self.LIKE, self.HATE)
    
    def likeHate(self):
        for y, rows in self.rowss.items():
            if y == self.goal:
                self.LIKE += len(rows)
            else:
                self.HATE += len(rows)


    def top(self, t):
        t.sort(key=lambda x: x.scored, reverse=True)  
        u = []
        for x in t:
            if x.scored >= t[0].scored * the['Cut']:
                u.append(x)
        return u[:the['beam']]
    
    def trys(self, ranges):
        u = []
        for subset in powerset(ranges):
            if len(subset) > 0:
                rule = Rule(subset)
                rule.scored = self.score(rule.selectss(self.rowss))
                if rule.scored > 0.01:
                    u.append(rule)
        return u
    
def powerset(s):
    t = [[]]
    for i in range(len(s)):
        for j in range(len(t)):
            t.append([s[i]] + t[j])
    return t

def score(t, goal, LIKE, HATE):
    like, hate, tiny = 0, 0, 1E-30
    for klass, n in t.items():
        if klass == goal:
            like += n
        else:
            hate += n 
    like, hate = like / (LIKE + tiny), hate / (HATE + tiny)
    if hate > like :
        return 0
    else:
        return like ** the['Support'] / (like + hate + tiny)