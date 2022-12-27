"""
--- Day 11: Corporate Policy ---
https://adventofcode.com/2015/day/11
"""
from aocd import data
import re

class Solution:
    def __init__(self) -> None:
        self.alphabet = "abcdefghjkmnpqrstuvwxyz"

    def req1(self, s) -> bool:
        """
        Passwords must include one increasing straight of at least three letters, 
        like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd 
        doesn't count.
        """
        for a, b, c in zip(s, s[1:], s[2:]):
            ord_a = ord(a)
            if (0, ord(b) % ord_a, ord(c) % ord_a) == (0, 1, 2):
                return True
        else:
            return False

    def req2(self, s) -> str:
        """
        Passwords may not contain the letters i, o, or l, as these letters can be 
        mistaken for other characters and are therefore confusing.
        """
        return "i" not in s and "o" not in s and "l" not in s

    def req3(self, s) -> int:
        """
        Passwords must contain at least two different, non-overlapping pairs of 
        letters, like aa, bb, or zz.
        """
        return len(re.findall(r"(.)\1", s)) >= 2

    def is_valid(self, passwd) -> bool:
        return self.req1(passwd) and self.req2(passwd) and self.req3(passwd)

    def preprocess(self ,s) -> str:
        result = ""
        for c in s:
            if c in "iol":
                result += {"i": "j", "o": "p", "l": "m"}[c]
                break
            else:
                result += c
        result += "a" * (8 - len(result))
        return result

    def next_password(self, s) -> str:
        s = self.preprocess(s)
        tr = dict(zip(self.alphabet, self.alphabet[1:]))
        while True:
            s_list = list(s)
            i = -1
            while True:
                try:
                    s_list[i] = tr[s_list[i]]
                except KeyError:
                    s_list[i] = "a"
                    i -= 1
                else:
                    break
            s = "".join(s_list)
            if self.is_valid(s):
                return s

if __name__ == "__main__":
    solve = Solution()
    first = solve.next_password(data)
    # Answer to Part One
    print(f"Part One: {first}")
    # Answer to Part Two
    second = solve.next_password(first)
    print(f"Part Two: {second}")