"""
Part One

Pair up the numbers and measure how far apart they are. 
Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are.
You'll need to add up all of those distances. 
For example, if you pair up a 3 from the left list with a 7 from the right list, 
the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

To find the total distance between the left list and the right list, 
add up the distances between all of the pairs you found. 

What is the total distance between your lists?

-------------------
Part Two

This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
Calculate a total similarity score by adding up each number in the left list after 
multiplying it by the number of times that number appears in the right list.

What is their similarity score?
"""

list_one = []
list_two = []

with open('input.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        nums = line.split("  ")
        list_one.append(int(nums[0].strip()))
        list_two.append(int(nums[1].strip()))

# Sort both lists
list_one.sort()
list_two.sort()

def part_one() -> int:
    """
    Sort lists, iterate and calculate difference for each set, add
    all differences.
    """
    diffs = 0
    for x, y in zip(list_one, list_two):
        diffs += abs(x - y)

    return diffs

def part_two() -> int:
    """
    For each number in list one, find how many times it appears in list two.
    Then, multiply that list one number by the amount of times it appears.
    Lastly, add all these products to find the final 'similarity score'.
    """
    similarity_score = 0
    l = 0
    r = 0
    n = len(list_one)
    m = len(list_two)

    # Use two pointers to iterate through lists
    while l < n and r < m:
        k = 0

        # Iterate left list until element is greater than or equal to the right list element.
        # 1 <-> 3
        # 2 <-> 3
        # 3 <-> 3
        while list_one[l] < list_two[r]:
            l += 1
            if l >= n:
                return similarity_score

        # If matching numbers, iterate right list to count duplicates.
        # 3 <-> 3
        # 3 <-> 3
        # 3 <-> 3
        while list_one[l] == list_two[r]:
            k += 1
            r += 1
            if r >= m:
                return similarity_score

        # Iterate right list until it is greater than or equal to the left list element.
        # 7 <-> 5
        # 7 <-> 6
        # 7 <-> 7
        while list_one[l] > list_two[r]:
            r += 1
            if r >= m:
                return similarity_score

        # Get the similarity score for this iteration
        # 3 <-> 3
        # 3 <-> 3   k = 3, similarity_score = 3 * 3
        # 3 <-> 3
        if k > 0:
            print(f'Found [{list_one[l]}] in list_two [{k}] times.')
            similarity_score += list_one[l] * k

    return similarity_score

def print_side_by_side():
    for i, j in zip(list_one, list_two):
        print(f'{i} : {j}')

print(f'Sum of differences: {part_one()}')
print(f'Similarity score: {part_two()}')
