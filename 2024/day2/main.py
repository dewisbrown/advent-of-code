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


"""

# Read input into list
reports = []
with open('input.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        report = line.strip().split(" ")
        reports.append(line.strip())

def part_one() -> int:
    safe_levels = 0



    return safe_levels

print(reports)