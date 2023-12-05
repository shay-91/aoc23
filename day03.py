def is_digit(c):
    return c >= '0' and c <= '9'

def is_symbol(lines, i, j):
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[i]):
        return False
    return not is_digit(lines[i][j]) and lines[i][j] != '.'

def get_number(lines, i, start):
    end = start
    while end < len(lines[i]) and is_digit(lines[i][end]):
        end+=1
    if start == end:
        return None
    else:
        return int(lines[i][start:end])
    
def is_part_number(lines, i, start, end):
    if is_symbol(lines, i, start-1) or is_symbol(lines, i, end):
        return True
    for j in range(start-1,end+1):
        if is_symbol(lines, i-1, j) or is_symbol(lines, i+1,j):
            return True
    return False

def part_one(lines):
    sum = 0
    lines = list(map(lambda x: x.strip(), lines))
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]):
            number = get_number(lines, i, j)
            if number == None:
                j+=1
            else:
                length = len(str(number))
                if is_part_number(lines,i,j, j+length):
                    sum += number
                j += length
    return sum

def part_two(lines):
    sum = 0
    return sum

input = open('input03.txt', 'r')
lines = input.readlines()
print(part_one(lines))
print(part_two(lines))