def transform(mapping, seeds):
    res = []
    for seed in seeds:
        mapped = False
        for f in mapping:
            start, end, offset = f
            if seed >= start and seed <= end:
                res.append(seed + offset)
                mapped = True
                break
        if not mapped:
            res.append(seed)
    return res
        

def part_one(lines):
    seeds = map(int, lines[0].split(':')[1].strip().split(' '))
    i = 3
    mapping = []
    while i < len(lines):
        if lines[i] == '\n':
            seeds = transform(mapping,seeds)
            mapping = []
            i += 2
        else:
            destination, source, length = (map(int,lines[i].strip().split(' ')))
            mapping.append((source, source+length-1, destination - source))
            i += 1
    seeds = transform(mapping,seeds)
    mapping = []
    i += 2
    return min(seeds)

def part_two(lines):
    return 0

input = open('input05.txt', 'r')
lines = input.readlines()
print(part_one(lines))
print(part_two(lines))