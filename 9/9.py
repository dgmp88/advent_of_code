# Get the data in 

test_data = open('test_data', 'r').readlines()
test_data = [td.strip() for td in test_data]
test_groups = [1, 3, 3, 6, 1, 1, 5, 2]

data = open('data', 'r').read()

def count_groups(data):
    groups = 0
    group_depth = 0
    in_garbage = 0
    idx = 0
    score = 0
    garbage = 0

    while idx < len(data):
        if data[idx] == '!':
            idx += 1
        elif in_garbage:
            if data[idx] == '>':
                in_garbage = False
            else:
                garbage += 1
        elif data[idx] == '<':
            in_garbage = True
        elif not in_garbage:
            if data[idx] == '{':
                group_depth += 1
            elif data[idx] == '}':
                groups += 1
                score += group_depth
                group_depth -= 1
        idx += 1

    return groups, score, garbage

for idx, line in enumerate(test_data):
    groups, score, garbage = count_groups(line)
    assert groups == test_groups[idx]

print(count_groups(data))
