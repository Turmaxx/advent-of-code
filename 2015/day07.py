"""
--- Day 7: Some Assembly Required ---
https://adventofcode.com/2015/day/7
"""
from aocd import data
import operator, re
import numpy as np

class Solution:
    def __init__(self) -> None:
        self.opmap = {
                "AND": operator.and_,
                "OR": operator.or_,
                "LSHIFT": operator.lshift,
                "RSHIFT": operator.rshift,
                }

    def compute(self, data) -> dict:
        result = {}
        lines = [line.split(" -> ") for line in data.splitlines()]

        def getval(v):
            return result[v] if v in result else np.uint16(v)

        def process_line(line):
            left, right = line
            left = left.split()
            len_left = len(left)
            if len_left == 1:
                # store
                result[right] = getval(left[0])
            elif len_left == 2:
                # negation
                op, val = left
                if op != "NOT":
                    raise Exception
                result[right] = ~getval(val)
            elif len_left == 3:
                a, op, b = left
                op = self.opmap[op]
                result[right] = op(getval(a), getval(b))

        while lines:
            line = lines.pop()
            try:
                process_line(line)
            except (KeyError, ValueError):
                lines = [line] + lines

        return result

if __name__ == "__main__":
    solve = Solution()
    result = solve.compute(data)
    result_a = result["a"]

    # Answer to Part One
    print(f"Part One: {result_a}")

    # Answer to Part Two
    new_data = re.sub(r"\n([0-9]+) -> b\n", f"\n{result_a} -> b\n", data)
    result_b = solve.compute(new_data)["a"]
    print(f"Part Two: {result_b}")
