# read data from text file
with open('input-text/day1.txt', encoding='utf-8') as file:
    data = file.readlines()


def get_num(line: str) -> int:
    digits = []

    for i in range(0, len(line)):
        if line[i].isdigit():
            digits.append(line[i])

    return int(digits[0] + digits[-1])


if __name__ == '__main__':
    nums = []
    for line in data:
        nums.append(get_num(line.strip()))
    
    print(sum(nums))
