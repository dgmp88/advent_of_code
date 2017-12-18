from functools import reduce

class CircularList:
    def __init__(self, list):
        self.list = list

    def get(self, start, end):
        return [self.list[idx % len(self)] for idx in range(start, end)]

    def set(self, start, end, list):
        for l_idx, idx in enumerate(range(start, end)):
            self.list[idx % len(self)] = list[l_idx]

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)

    def cap(self, var):
        return var % len(self)

class Numbers:
    def __init__(self, data, lengths):
        self.list = CircularList(data)
        self.current_pos = 0
        self.skip_size = 0
        self.lengths = lengths
        self.data_length = len(data)

    def process_lengths(self):
        for l in self.lengths:
            self.reverse(l)
            self.current_pos += l + self.skip_size
            self.skip_size += 1

    def reverse(self, length):
        start, end = self.current_pos, self.current_pos + length
        data = self.list.get(start, end)
        data.reverse()
        self.list.set(start, end, data)

    def __str__(self):
        return str(self.list)

    def result(self):
        return self.list.list[0] * self.list.list[1]

class String:
    def __init__(self, data, lengths):
        self.list = CircularList(data)
        self.current_pos = 0
        self.skip_size = 0
        lengths = [ord(str(i)) for i in lengths]
        lengths.extend([17, 31, 73, 47, 23])

        self.lengths = lengths
        self.data_length = len(data)
        for i in range(64):
            self.process_lengths()

        self.compute_dense_hash()
        self.compute_hex()

    def process_lengths(self):
        for l in self.lengths:
            self.reverse(l)
            self.current_pos += l + self.skip_size
            self.skip_size += 1

    def reverse(self, length):
        start, end = self.current_pos, self.current_pos + length
        data = self.list.get(start, end)
        data.reverse()
        self.list.set(start, end, data)

    def __str__(self):
        return str(self.list)

    def result(self):
        return self.list.list[0] * self.list.list[1]

    def compute_dense_hash(self):
        res = []
        step = 16
        for i in range(0, len(self.list), step):
            block = self.list.list[i:i+step]
            dense = reduce(lambda x, y: x ^ y, block)
            res.append(dense)
        self.dense_hash = res

    def compute_hex(self):
        self.hex = ''.join(['%0.2x' % val for val in self.dense_hash])

if __name__ == '__main__':
    t = Numbers(list(range(5)), [3, 4, 1, 5])
    t.process_lengths()
    print(t)
    assert t.result() == 12

    d = Numbers(list(range(256)), [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63])
    d.process_lengths()
    print('Result 1', d.result())
    
    for val in ['', 'AoC 2017', '1,2,3', '1,2,4']:
        t = String(list(range(256)), val)
        print(t.hex)


    t = String(list(range(256)), '197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63')
    print(t.hex)
