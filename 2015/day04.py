"""
--- Day 4: The Ideal Stocking Stuffer ---
https://adventofcode.com/2015/day/4
"""
from aocd import data
from _md5 import md5

class Solution:
    def mine(self, data, difficulty, start=0):
        secret_key = data.encode()
        prefix = "0" * difficulty
        h0 = md5(secret_key).copy
        i = start
        while True:
            i += 1
            hash_ = h0()
            hash_.update(b"%d" % i)
            if hash_.hexdigest().startswith(prefix):
                return i

if __name__ == "__main__":
    solve = Solution()
    a = solve.mine(data, difficulty=5)
    print(f"Part One: {a}")
    b = solve.mine(data, difficulty=6, start=a - 1)
    print(f"Part Two: {b}")
