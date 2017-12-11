import data

rules = {
    'inc': lambda a, b: a + b,
    'dec': lambda a, b: a - b,
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b, 
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b,
        }

class Line():
    def __init__(self, line):
        self.register, change, change_val, if_, self.other_register, rule, rule_val = line.split(' ')
        self.change = rules[change]
        self.change_val = int(change_val)
        self.rule = rules[rule]
        self.rule_val = int(rule_val)

    def apply(self, registers):
        if self.rule(registers.get(self.other_register), self.rule_val):
            new_val = self.change(registers.get(self.register), self.change_val)
            registers.set(self.register, new_val)

class Registers():
    def __init__(self, text):
        self.registers = {}
        self.lines = []
        self.max_ever = 0
        self.parse(text)

    def parse(self, text):
        for line in text.split('\n'):
            line = Line(line)
            self.lines.append(line)
            line.apply(self)
            new_val = self.get(line.register)
            if new_val > self.max_ever:
                self.max_ever = new_val


    def get(self, name):
        try:
            return self.registers[name]
        except KeyError:
            self.set(name, 0)
            return self.registers[name]

    def set(self, name, val):
        self.registers[name] = val

    def max(self):
        return max(list(self.registers.values()))


t = Registers(data.test_data)
assert t.max() == 1

d = Registers(data.data)
print('Max value = ', d.max())

assert t.max_ever == 10
print('Max ever = ', d.max_ever)
