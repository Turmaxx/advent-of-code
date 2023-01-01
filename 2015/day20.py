"""
--- Day 20: Infinite Elves and Infinite Houses ---
https://adventofcode.com/2015/day/20
"""
import numpy as np
from aocd import data

class Solution:
    A = np.zeros(1000000, dtype=int)
    B = A.copy()
    
    def infinite_elves(self):
        for i in range(1, 1000000):
            self.A[i::i] += i * 10
            self.B[i::i][:50] += i * 11

if __name__ == "__main__":
    solve = Solution()
    assert solve.A[1:10].tolist() == [10, 30, 40, 70, 60, 120, 80, 150, 130]
    # Answer to Part One
    print(f"Part One: {np.argmax(solve.A > int(data))}")
    # Answer to Part Two
    print(f"Part One: {np.argmax(solve.A > int(data))}")