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
    tokens_with_indices = parse_line(text)
    #print(tokens_with_indices)
    first = tokens_with_indices[0][0]
    last = tokens_with_indices[-1][0]

    return (my_dict[first] * 10) + my_dict[last]


def parse_line(text: str) -> list:
    current_lexeme = ''
    res = []
    i = 0
    n = len(text)

    while (i < n):
        while (i != n and text[i].isdigit()):
            res.append([text[i], i])
            current_lexeme = ''
            i += 1
        if i == n:
            break
        current_lexeme += text[i]
        if is_token(current_lexeme):
            token = get_token(current_lexeme)
            res.append([token, i - len(current_lexeme) + current_lexeme.index(token) + 1])
            current_lexeme = ''
        i += 1
    return res


def is_token(text: str) -> bool:
    for key in my_dict.keys():
        if key in text:
            return True
    return False


def get_token(text):
    for key in my_dict.keys():
        if key in text:
            return key


if __name__ == '__main__':
    part_one = 0
    part_two = 0
    for line in data:
        part_one += get_num(line.strip())
        part_two += get_num_with_str(line.strip())

    print(part_one)
    print(part_two) # wrong answers: 53859, 53900
