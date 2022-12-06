""" https://adventofcode.com/2022/day/1 """
import os

path_to_file = os.path.join(os.path.dirname(__file__), "day1_input.txt")

def solution():
    with open(path_to_file) as handle:
        all_packs = handle.read().split('\n')

    separators, packsums, start_span = [i for i in range(len(all_packs)) if all_packs[i] == ''], [], 0
    for end_span in separators: 
        packsums.append(sum([int(cal) for cal in all_packs[start_span:end_span]])) 
        start_span = end_span +1

    # Part 1
    print(f"The largest calorie package is worth {str(sorted(packsums)[-1])} calories.")
    # Part 2
    print(f"The largest three calorie packages combined are worth {str(sum(sorted(packsums)[-3:]))} calories.")

if __name__ == "__main__":
    solution()
