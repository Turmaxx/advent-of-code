"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
https://adventofcode.com/2015/day/3
"""
from aocd import data

class Solution:
    def __init__(self) -> None:
        self.step = {
            "^": -1j,
            ">": 1,
            "v": 1j,
            "<": -1,
        }

    def spherical(self, data, part_two=False) -> None:
        if part_two:
            z = 0
            seen = {z}
            for c in data[0::2]:  # santa
                z += self.step[c]
                seen |= {z}

            z = 0
            for c in data[1::2]:  # robo-santa
                z += self.step[c]
                seen |= {z}

            print("Part Two:", len(seen))

        else:
            z = 0
            seen = {z}
            for c in data:
                z += self.step[c]
                seen |= {z}

            print("Part One:", len(seen))

if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    solve.spherical(data)
    # Answer to Part Two
    solve.spherical(data, part_two=True)
