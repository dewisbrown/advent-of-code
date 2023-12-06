# read data from text file
with open('input-text/day1.txt', encoding='utf-8') as file:
    data = file.readlines()


def get_num(text: str) -> int:
    '''Extracts 2 digit number from line of text.'''
    digits = []

    for c in text:
        if c.isdigit():
            digits.append(c)

    return int(digits[0] + digits[-1])


if __name__ == '__main__':
    nums = []
    for line in data:
        nums.append(get_num(line.strip()))

    print(sum(nums))
