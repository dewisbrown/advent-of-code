"""
Part One

The unusual data (your puzzle input) consists of many reports, one report per line. 
Each report is a list of numbers called levels that are separated by spaces.

The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. 
So, a report only counts as safe if both of the following are true:
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.

Analyze the unusual data from the engineers. How many reports are safe?
----------------
Part Two

Now, the same rules apply as before, 
except if removing a single level from an unsafe report would make it safe, 
the report instead counts as safe.

Update your analysis by handling situations where the Problem Dampener 
can remove a single level from unsafe reports. How many reports are now safe?
"""

# Read input into list
reports = []
with open('input.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        report = [int(n) for n in line.strip().split(" ")]
        reports.append(report)

unsafe_reports = []

def part_one() -> int:
    """
    Iterate through input to find safe reports. Uses helper function.
    """
    safe_levels = 0

    for report in reports:
        if is_safe_one(report):
            safe_levels += 1

    return safe_levels

def part_two() -> int:
    """
    Uses other helper function to determine if report is safe.
    """
    safe_levels = 0

    for report in reports:
        if is_safe_one(report):
            safe_levels += 1
        elif is_safe_two(report):
            safe_levels += 1
    
    return safe_levels

def is_safe_one(report: list[int]) -> bool:
    """
    Logic to check if a report is 'safe'.
    """
    ascending = False

    # Check if ascending or descending
    if report[0] < report[1]:
        ascending = True
    
    # Iterate through report looking for:
    # - change from ascending to descending and vise versa
    # - difference is greater than three
    # - duplicate numbers
    for i in range(len(report) - 1):
        if ascending:
            if report[i] > report[i + 1]:
                return False
        else:
            if report[i] < report[i + 1]:
                return False
        if abs(report[i] - report[i + 1]) > 3:
            return False
        if report[i] == report[i + 1]:
            return False
    return True

def is_safe_two(report: list[int]) -> bool:
    """
    The same rules of part one apply to this check, with the 
    added rule of being able to remove an element to make it safe.
    """
    

    return is_safe_one(report)

print(f'Part two: {part_two()}')
