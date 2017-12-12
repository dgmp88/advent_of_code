# THIS DOESN'T WORK! MUST BE THE OTHER KEY BELOW!
#    0
#  \ n  /
#nw +--+ ne 1
#  /    \
#-+      +-
#  \    /
#sw +--+ se  2
#  / s  \

key = {'n': [1, 0, 0],
        'ne': [0, 1, 0], 
        'se': [0, 0, 1],
        's': [-1, 0, 0],
        'sw': [0, -1, 0],
        'nw': [0, 0, -1]}

# 0      1 
#  \ n  /
#nw +--+ ne 
#  /    \
#-+      +- 2 
#  \    /
#sw +--+ se 
#  / s  \

key = {'n': [1, 1, 0],
        'ne': [0, 1, 1], 
        'se': [-1, 0, 1],
        's': [-1, -1, 0],
        'sw': [0, -1, -1],
        'nw': [1, 0, -1]}
      

class Grid():
    def __init__(self, directions):
        self.pos = [0, 0, 0]
        self.furthest = 0
        for d in directions.split(','):
            self.move(d)

    def move(self, direction):
        for i in range(3):
            self.furthest = max(self.furthest, self.dist())
            self.pos[i] += key[direction][i]

    def dist(self):
        return max([abs(i) for i in self.pos])
    
tests = [('ne,ne,ne', 3),
        ('ne,ne,sw,sw', 0),
        ('ne,ne,s,s', 2),
        ('se,sw,se,sw,sw', 3)]

for test in tests:
    g = Grid(test[0])
    assert g.dist() == test[1], test

data = open('data').read().strip()

g = Grid(data)
print('Result 1: ', g.dist())
print('Result 2: ', g.furthest)
