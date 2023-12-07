'''Advent of Code Day 1 - https://adventofcode.com/2023/day/1'''

my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

# read data from text file
with open('input-text/day1.txt', encoding='utf-8') as file:
    data = file.readlines()

# part one
def get_num(text: str) -> int:
    '''Extracts 2 digit number from line of text.'''
    digits = []

    for c in text:
        if c.isdigit():
            digits.append(c)

    if digits:
        return int(digits[0] + digits[-1])
    return 0


# part two
def get_num_with_str(text: str) -> int:
    '''Extracts digits from line of text, also checks spelled out numbers.'''
    numbers = {}

    for key in my_dict.keys():
        if key in text:
            numbers[key] = text.index(key)

    for index, c in enumerate(text):
        if c.isdigit():
            numbers[c] = index

    sorted_by_value = sorted(numbers.items(), key=lambda x:x[1])
    first = sorted_by_value[0][0]
    last = sorted_by_value[-1][0]

    return (my_dict[first] * 10) + my_dict[last]

if __name__ == '__main__':
    part_one = 0
    part_two = 0
    for line in data:
        part_one += get_num(line.strip())
        part_two += get_num_with_str(line.strip())

    print(part_one)
    print(part_two) # 53859
