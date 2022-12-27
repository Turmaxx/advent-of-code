"""
--- Day 8: Matchsticks ---
https://adventofcode.com/2015/day/8
"""
from aocd import data

class Solution:
    def tokens(self, s):
        iterator = iter(s)
        for char in iterator:
            if char == "\\":
                char += next(iterator)
                if char.endswith("x"):
                    char += next(iterator)
                    char += next(iterator)
            yield char

    def encoder(self, s):
        iterator = iter(s)
        yield '"'
        for char in iterator:
            if char == '"' or char == "\\":
                yield "\\"
            yield char
        yield '"'

    def tokens_len(self, s):
        return sum(1 for token in self.tokens(s)) - 2

    def length_diff(self, data):
        return sum(len(line) - self.tokens_len(line) for line in data.splitlines())

    def encoded_diff(self, data):
        return sum(len("".join(self.encoder(line))) - len(line) for line in data.splitlines())

if __name__ == "__main__":
    solve = Solution()
    # Anwer to Part One
    print(f"Part One: {solve.length_diff(data)}")
    # Anwer to Part Two
    print(f"Part Two: {solve.encoded_diff(data)}")
