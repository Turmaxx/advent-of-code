""" https://adventofcode.com/2022/day/4 """
import os

path_to_file = os.path.join(os.path.dirname(__file__), "day4_input.txt")

class CampCleaner:
    def __init__(self, test=False):
        self.input = path_to_file
        with open(self.input, 'r') as f:
            sections_to_clean = [[range(int(sections.split('-')[0]), int(sections.split('-')[1]) + 1) for sections in line.split(',')]
                                 for line in f]

        self.groups = sections_to_clean

    def part_one(self):
        """Count pairs of assignments where one range fully contains the other."""
        return sum(set(range_1).issubset(range_2) or set(range_2).issubset(range_1) for range_1, range_2 in self.groups)

    def part_two(self):
        """Count pairs of assignments where both range overlap."""
        return sum(len(set(range_1).intersection(range_2)) > 0 for range_1, range_2 in self.groups)

if __name__ == '__main__':
    print('Part One:', CampCleaner().part_one())
    print('Part Two:', CampCleaner().part_two())
