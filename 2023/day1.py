'''Advent of Code Day 1 - https://adventofcode.com/2023/day/1'''

text_to_nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
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

    return int(digits[0] + digits[-1])


# part two
def get_num_with_str(text: str) -> int:
    digits = []

    for c in text:
        digits.append(c)

    return int(digits[0] + digits[-1])

if __name__ == '__main__':
    nums = []
    for line in data:
        nums.append(get_num(line.strip()))

    print(sum(nums))
