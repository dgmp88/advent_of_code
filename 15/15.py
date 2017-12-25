

def trans(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

class Generator():
    div = 2147483647
    def __init__(self, factor, value):
        self.factor = factor
        self.value = value
    
    def next(self):
        self.value = (self.value * self.factor) % self.div
        return self
    
    def bin(self):
        binary = bin(self.value)

        if len(binary) >= 18:
            return binary[-16:]
        else:
            binary = binary[2:]
            while len(binary) != 16:
                binary = '0' + binary
            return binary

class Judge():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.tot = 0
        
    def match(self):
        self.next()
        a_ = self.a.bin()
        b_ = self.b.bin()
        if a_ == b_:
            self.tot += 1

    def run(self, iterations):
        for i in range(iterations):
            self.match()
        return self.tot
        
    def next(self):
        self.a.next(), self.b.next()

        
def init():    
    a = Generator(16807, 65)
    b = Generator(48271, 8921)
    return Judge(a, b)

assert init().run(5) == 1

init().run(int(1e6))

