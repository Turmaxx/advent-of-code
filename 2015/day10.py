"""
--- Day 10: Elves Look, Elves Say ---
https://adventofcode.com/2015/day/10
"""
from aocd import data
from itertools import groupby

class Solution:
    def look_and_say(self, s, n=1):
        for _ in range(n):
            s = "".join([f"{len(list(group))}{key}" for key, group in groupby(s)])
        return s

if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    a = solve.look_and_say(data, n=40)
    print(f"Part One: {len(a)}")
    # Answer to Part Two
    b = solve.look_and_say(a, n=10)
    print(f"Part Two: {len(b)}")