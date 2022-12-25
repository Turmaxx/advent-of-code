""" 
--- Day 1 - Calorie Counting ---
https://adventofcode.com/2022/day/1 
"""

from aocd import data
from heapq import nlargest

class Solution:
    def calories(self, part_two=False) -> None:
        """
        Counting Calories 
        """
        cals = [sum(map(int, chunk.split())) for chunk in data.split("\n\n")]

        if part_two:
            print(f"Part Two: {sum(nlargest(3, cals))}")
        else:
            print(f"Part One: {max(cals)}")

if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    solve.calories()
    # Answer to Part Two
    solve.calories(part_two=True)