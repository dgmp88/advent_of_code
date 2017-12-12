import data

def parse_to_dict(data):
    programs = {}
    for line in data.split('\n'):
        key, values =  line.split(' <-> ')
        key = int(key)
        values = tuple((int(v) for v in values.split(',')))
        programs[key] = values
    return programs

def count_connections(data):
    programs = parse_to_dict(data) 
    return len(expand_group(programs, 0)) 

def expand_group(programs, start):
    visited = set()
    tovisit = set([start])
    while len(tovisit) > 0:
        on = tovisit.pop()
        for item in programs[on]:
            if item not in visited:
                visited.add(item)
                tovisit.add(item)
    return visited

def count_groups(data):
    programs = parse_to_dict(data) 
    groups = []
    unvisited = list(programs.keys())
    while len(unvisited) > 0:
        start = unvisited[0]
        group = expand_group(programs, start)
        groups.append(group)
        for item in group:
            unvisited.remove(item)
    return len(groups)

assert count_connections(data.test_data) == 6
print('Results 1: ', count_connections(data.data))

assert count_groups(data.test_data) == 2
print('Results 2: ', count_groups(data.data))
