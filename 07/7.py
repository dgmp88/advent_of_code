import data
import re

class Program():
    def __init__(self, name, weight, over_txt):
        self.name = name
        self.weight = int(weight)
        self.over_txt = over_txt
        self.under = None
        self.over = []
        self.tot_weight = None

    def __eq__(self, other):
        if isinstance(other, Program):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other

    def link_over(self, programs):
        for over_txt in self.over_txt:
            over = programs[over_txt]
            over.under = self
            self.over.append(over)

    def __str__(self):
        return 'Program {name} weight {weight}'.format(name=self.name, weight=self.weight)

    def get_siblings(self):
        return self.under.over

    def is_weighable(self):
        if len(self.over) == 0:
            self.tot_weight = self.weight
            return True
        else:
            for prog in self.over:
                if prog.tot_weight is None:
                    return False
            return True

    def weigh(self):
        if self.tot_weight == None:
            self.tot_weight = sum([c.weigh() for c in self.over]) + self.weight
        return self.tot_weight

    def print_under(self, indent):
        print(indent + '{name}, {tot_weight}'.format(name=self.name, tot_weight = self.tot_weight))
        indent += '\t'
        for o in self.over:
            o.print_under(indent)

    def get_uneven_over(self):
        over_weights = [o.tot_weight for o in self.over]
        odd_num = get_odd(over_weights)
        if not odd_num:
            return self
        odd_prog = self.over[over_weights.index(odd_num)]
        return odd_prog.get_uneven_over()


def get_odd(lst):
    for item in lst:
        if lst.count(item) != len(lst):
            if lst.count(item) == 1:
                return item
    return False

class Tree():
    def __init__(self, text):
        self.programs = {}
        self.parse_data(text)
    
    def parse_data(self, text):
        # Create all programs
        for line in text.split('\n'): 
            names = re.findall('[a-z]+', line)
            weight = re.findall('([0-9]+)', line)[0]
            name = names[0]
            self.programs[name] = Program(name, weight, names[1:])
        
        # Make links
        for name, prog in self.programs.items():
            prog.link_over(self.programs) 

    def get_first_program(self):
        return next(iter(self.programs.values()))

    def get_bottom(self):
        # Pick a random node, and go to unders until there are none left
        program = self.get_first_program()
        while program.under is not None:
            program = program.under
        return program

    def get_correct_weight(self):
        # Start by getting all items at the top, and work down the tree
        bottom = self.get_bottom()
        bottom.weigh()

        # Get the uneven child
        dodgy = bottom.get_uneven_over()
        sibs = dodgy.get_siblings()
        sibs.remove(dodgy)
        desired_weight = sibs[0].tot_weight
        actual_weight = dodgy.tot_weight
        diff = actual_weight - desired_weight 
        
        return dodgy.weight - diff

    
    def get_tops(self):
        tops = filter(lambda x: len(x.over) == 0, self.programs.values())
        tops = list(tops)
        return tops

t = Tree(data.test_data)

assert t.get_bottom().name == 'tknk'

d = Tree(data.data)
print('Bottom program: ', d.get_bottom())

assert t.get_correct_weight() == 60
print('Correct weight: ', d.get_correct_weight())
