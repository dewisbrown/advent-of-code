# read data from text file
with open('input-text/day8.txt', encoding='utf-8') as file:
    data = file.readlines()


# use two pointers to check rows, figure out how to check columns
for line in data:
    l: int = 0
    r: int = len(line.strip()) - 1

    left_list: list = []
    right_list: list = []

    while (l < r):
        left_height: int = line[l]
        right_height: int = line[r]

        # something
        l += 1

        # something
        r -= 1
