"""
--- Day 1: Not Quite Lisp ---
https://adventofcode.com/2015/day/1
"""
from aocd import data

class Solution:
    def direction(self, part_two=False) -> None:

        order = { 
            "(" : +1,
            ")" : -1,
        }

        basement, floor = None, 0

        for i, c in enumerate(data, 1):
            floor += order[c]
            if basement is None and floor == -1:
                basement = i

        if part_two:
            print(f"First Time in Basement = {basement}")
        else:
            print(f"Final Floor = {floor}")

if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    solve.direction()
    # Answer to Part Two
    solve.direction(part_two=True)
