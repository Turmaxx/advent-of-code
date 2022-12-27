"""
--- Day 9: All in a Single Nigth ---
https://adventofcode.com/2015/day/9
"""
from aocd import data
from itertools import permutations

class Solution:
    def parsed(self, data):
        distances = {}
        cities = set()
        for line in data.splitlines():
            a, _, b, _, n = line.split()
            cities |= {a, b}
            distances[(a, b)] = distances[(b, a)] = int(n)
        return cities, distances

    def total_distances(self, route, distances):
        return sum(distances[p] for p in zip(route[:-1], route[1:]))

    def get_routes(self, data):
        cities, distances = self.parsed(data)
        return {route: self.total_distances(route, distances) for route in permutations(cities)}


if __name__ == "__main__":
    solve = Solution()
    routes = solve.get_routes(data)
    # Answer to Part One
    print(f"Part One: {min(routes.values())}")
    # Answer to Part Two
    print(f"Part One: {max(routes.values())}")