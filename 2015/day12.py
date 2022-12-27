"""
--- Day 12: JSAbacusFramework.io ---
https://adventofcode.com/2015/day/12
"""
from aocd import data
import json, re

class Solution:
    def sum_of_numbers_in_text(self, s):
        return sum(int(n) for n in re.findall(r"-?\d+", s))

    def rsum(self, data):
        if isinstance(data, int):
            return data
        elif isinstance(data, dict):
            if "red" in data.values():
                return 0
            return self.rsum(list(data.values()))
        elif isinstance(data, list):
            return sum(self.rsum(n) for n in data)
        else:
            return 0

if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    print(f"Part One: {solve.sum_of_numbers_in_text(data)}")
    # Answer to Part Two
    print(f"Part Two: {solve.rsum(json.loads(data))}")
