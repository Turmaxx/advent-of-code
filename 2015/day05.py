"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
https://adventofcode.com/2015/day/5
"""
from aocd import data

class Solution:
    def __init__(self) -> None:
        self.words = data.splitlines()
    
    def vowel_count(self, s):
        vowels = set("aeiou")
        return sum(1 for c in s if c in vowels)

    def has_double(self, s):
        for left, right in zip(s[:-1], s[1:]):
            if left == right:
                return True

    def blacklisted(self, s):
        for substring in "ab", "cd", "pq", "xy":
            if substring in s:
                return True

    def has_pair(self, s):
        for left, right in zip(s[:-1], s[1:]):
            if s.count(left + right) > 1:
                return True

    def has_skip_repeat(self, s):
        for left, right in zip(s[:-2], s[2:]):
            if left == right:
                return True

    def is_nice_a(self, s):
        return self.vowel_count(s) >= 3 and self.has_double(s) and not self.blacklisted(s)

    def is_nice_b(self, s):
        return self.has_pair(s) and self.has_skip_repeat(s)

    def part_one(self):
        print("Part One:", len([w for w in self.words if self.is_nice_a(w)]))

    def part_two(self):
        print("Part Two:", len([w for w in self.words if self.is_nice_b(w)]))

if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    solve.part_one()
    # Answer to Part Two
    solve.part_two()
