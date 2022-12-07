""" https://adventofcode.com/2022/day/2 """
import os

path_to_file = os.path.join(os.path.dirname(__file__), "day2_input.txt")

ordered_scores_part1 = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
ordered_scores_part2 = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]

def get_score(input_list):
    with open(path_to_file) as handle:
        return sum(map(lambda pair: input_list.index(pair) + 1, map(lambda line: ''.join(line.strip().split()), handle.readlines())))

if __name__ == "__main__":
    print(f"Part 1: {get_score(ordered_scores_part1)}")
    print(f"Part 2: {get_score(ordered_scores_part2)}")
