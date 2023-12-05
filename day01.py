def getNumber(line):
    if line[0] >= '0' and line[0] <= '9':
        return int(line[0])
    if line[:3] == 'one':
        return 1
    if line[:3] == 'two':
        return 2
    if line[:5] == 'three':
        return 3
    if line[:4] == 'four':
        return 4
    if line[:4] == 'five':
        return 5
    if line[:3] == 'six':
        return 6
    if line[:5] == 'seven':
        return 7
    if line[:5] == 'eight':
        return 8
    if line[:4] == 'nine':
        return 9
    return None

def part_one(lines):
    sum = 0
    for line in lines:
        for char in line:
            if char >= '0' and char <= '9':
                sum += int(char) * 10
                break
        
        for char in line[::-1]:
            if char >= '0' and char <= '9':
                sum += int(char)
                break
    return sum

def part_two(lines):
    sum = 0
    for line in lines:
        numbers = []
        for i in range(len(line)):
            number = getNumber(line[i::])
            if number != None:
                numbers.append(number)
        sum += numbers[0] * 10 + numbers[len(numbers)-1]
    return sum

input = open('input01.txt', 'r')
lines = input.readlines()
print(part_one(lines))
print(part_two(lines))