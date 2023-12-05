def part_one(lines):
    sum = 0
    for line in lines:
        winning_numbers, numbers = line.split(':')[1].split('|')
        numbers = numbers.strip().split(' ')
        numbers = filter(lambda x: x != '', numbers)
        numbers = list(map(int, numbers))
        winning_numbers = winning_numbers.strip().split(' ')
        winning_numbers = filter(lambda x: x != '', winning_numbers)
        winning_numbers = list(map(int, winning_numbers))
        hits = 0
        for number in numbers:
            if number in winning_numbers:
                hits += 1
        sum += 0 if hits == 0 else 2**(hits - 1)
    return sum

def part_two(lines):
    sum = 0
    cards = []
    for line in lines:
        winning_numbers, numbers = line.split(':')[1].split('|')
        numbers = numbers.strip().split(' ')
        numbers = filter(lambda x: x != '', numbers)
        numbers = list(map(int, numbers))
        winning_numbers = winning_numbers.strip().split(' ')
        winning_numbers = filter(lambda x: x != '', winning_numbers)
        winning_numbers = list(map(int, winning_numbers))
        cards.append((1, winning_numbers, numbers))
    for i in range(len(cards)):
        amount, winning_numbers, numbers = cards[i]
        sum += amount
        hits = 0
        for number in numbers:
            if number in winning_numbers:
                hits += 1
        for j in range(1,hits+1):
            if i + j < len(cards):
                amount_f, winning_numbers_f, numbers_f = cards[i+j]
                cards[i+j] = amount_f + amount, winning_numbers_f, numbers_f
    return sum

input = open('input04.txt', 'r')
lines = input.readlines()
print(part_one(lines))
print(part_two(lines))