"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4
"""

from aocd import data
from parse import parse

class Solution:
    def camp_cleaner(self, a, b) -> int:
        for line in data.splitlines():
            l1, r1, l2, r2 = parse("{:d}-{:d},{:d}-{:d}", line).fixed
            if l1 > l2 or (l1 == l2 and r1 < r2):
                l1, r1, l2, r2 = l2, r2, l1, r1
            a += r2 <= r1
            b += r1 >= l2
        
        return a, b

if __name__ == "__main__":
    solve = Solution() 
    a = b = 0
    a, b = solve.camp_cleaner(a,b)

    print(f"Part One : {a}")
    print(f"Part Two : {b}")
