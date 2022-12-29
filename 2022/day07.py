"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7
"""
from aocd import data
from pathlib import Path
from collections import Counter

    
cwd = root = Path("/")
dirs = Counter()

class Solution:
    def no_space(self, data):
        for line in data.splitlines():
            match line.split():
                case ["$", "cd", "/"]: cwd = root
                case ["$", "cd", ".."]: cwd = cwd.parent
                case ["$", "cd", name]: cwd /= name
                case [s, name] if s.isdigit():
                    for p in [cwd, *cwd.parents]:
                        dirs[p] += int(s)

        rmbytes = dirs[root] - 70_000_000 + 30_000_000
        a = sum(v for v in dirs.values() if v <= 100_000)
        b = min(v for v in dirs.values() if v >= rmbytes)

        return a, b


if __name__ == "__main__":
    solve = Solution()
    a, b = solve.no_space(data)
    # Answer to Part One
    print(f"Part One: {a}")
    # Answer to Part Two
    print(f"Part Two: {b}")
