import data

class Pipe:
    def __init__(self, a, b):
        self.a, self.b = a, b
        
    def has(self, num):
        return num == self.a or num == self.b
    
    def __str__(self):
        return '{0}/{1}'.format(self.a, self.b)
    
    def __lt__(self, other):
        return self.a <= other.a and self.b < other.b
    
    def get_other(self, num):
        return self.a if num != self.a else self.b
    
class Parts: 
    def __init__(self, parts=None):
        if parts == None:
            parts = []
        parts.sort()
        self.parts = parts
    
    def remove(self, part):
        self.parts.remove(part)
    
    def add(self, part):
        self.parts.append(part)
        self.parts.sort()

    def make_bridges(self):
        depth = 0
        connection = 0 # Have to connect to a 0 to start with
        
        bridges = []
        bridge = Bridge()
        
        available = Parts(self.parts.copy())
        branch_choices = []
        
        while True:
            next_part = self.get_next(bridge, branch_choices, available)
            if next_part == False:
                bridges.append(bridge.copy())
                if len(branch_choices) == 0:
                    break
            else:
                bridge.add(next_part)
            print('bridge: ', bridge)
        print('*'*20)

        for bridge in bridges:
            print(bridge)
            
    def get_next(self, prefix, branch_choices, available):
        while True:
            depth = len(prefix)

            # If we haven't seen this branch yet, pick the first value
            if depth == len(branch_choices):
                branch_choices.append(0)

            # Items with the right connections
            next_available = available.get_has(prefix.connection)
            
            if len(next_available) <= branch_choices[depth]:
                # If we've exhausted this end, go back
                branch_choices.pop()
                end = prefix.remove()
                available.add(end)
                return False
            
            print('OK to go, depth: ', depth, 'bcd', branch_choices[depth], 'bc', branch_choices)
            if branch_choices[depth] == 1:
                1/0
            use = next_available[branch_choices[depth]]
            available.parts.remove(use)
            branch_choices[depth] += 1
            return use
    
    def get_has(self, a):
        has = []        
        for p in self.parts:
            if p.has(a):
                has.append(p)
        return has
    
    def __str__(self):
        s = ''
        for pipe in self.parts:
            s += str(pipe) + '\t'
        return s

    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.parts)
    
    def copy(self):
        return Parts(self.parts.copy())
    
class Bridge(Parts):
    def __init__(self):
        self.parts = []
        self.connection = 0
    
    def remove(self):
        end = self.parts[-1]
        self.parts.remove(end)
        self.connection = end.get_other(self.connection)
        return end
    
    def add(self, part):
        self.parts.append(part)
        self.connection = part.get_other(self.connection)

def parse_text(data):
    parts = []

    for pipe in data.split('\n'):
        a, b = pipe.split('/')
        parts.append(Pipe(int(a), int(b)))

    return Parts(parts)

t = parse_text(data.test_data)
t.make_bridges()
