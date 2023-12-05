def part_one(lines):
    sum = 0
    for line in lines:
        game, sets = line.split(':')
        id = int(game.split(' ')[1])
        green = 0; red = 0; blue = 0
        sets = sets.split(';')
        for set in sets:
            subsets = map(lambda x : x.strip(), set.split(', '))
            for subset in subsets:
                amount, color = subset.split(' ')
                match color:
                    case 'green':
                        green = max(green,int(amount))
                    case 'blue':
                        blue = max(blue, int(amount))
                    case other:
                        red = max(red, int(amount))
        if red <= 12 and green <= 13 and blue <= 14:
            sum += id
    return sum

def part_two(lines):
    sum = 0
    for line in lines:
        game, sets = line.split(':')
        id = int(game.split(' ')[1])
        green = 0; red = 0; blue = 0
        sets = sets.split(';')
        for set in sets:
            subsets = map(lambda x : x.strip(), set.split(', '))
            for subset in subsets:
                amount, color = subset.split(' ')
                match color:
                    case 'green':
                        green = max(green,int(amount))
                    case 'blue':
                        blue = max(blue, int(amount))
                    case other:
                        red = max(red, int(amount))
        
        sum += green * red * blue
    return sum


input = open('input02.txt', 'r')
lines = input.readlines()
print(part_one(lines))
print(part_two(lines))