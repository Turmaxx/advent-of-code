"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""
from aocd import data
from collections import Counter


class Solution:
    def marker(self, data, n):
        counts = Counter(data[:n])
        i = n
        while len(counts) < n:
            if data[i] != data[i - n]:
                counts += {data[i]: 1, data[i - n]: -1}
            i += 1
        return i


if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    print(f"Part One: {solve.marker(data, 4)}")
    # Answer to Part Two
    print(f"Part Two: {solve.marker(data, 4)}")
