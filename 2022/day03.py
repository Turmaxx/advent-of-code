""" 
--- Day 3 - Rucksack Reorganization ---
https://adventofcode.com/2022/day/3 
"""

from aocd import data

class Solution:
    
    def read(self):
        return list(filter(None, data.split('\n'))), 0

    def solution1(self):
        # Part 1
        rucksacks, priority_sum = self.read()
        for rucksack in rucksacks: 
            compartment_a,compartment_b  = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):] 
            common_item = [i for i in compartment_a
            if i in compartment_b][0] 
            priority_sum += ord(common_item) - (38 if common_item.isupper() else 96)
      
        print(f"The sum of priority item values is: {str(priority_sum)}")
     
    def solution2(self):
        # Part 2
        rucksacks, groups_priority_sum = self.read()
        for i in range(0, len(rucksacks), 3): 
            elf_group = rucksacks[i:i+3] 
            badge = [x for x in elf_group[0] if x in elf_group[1] and x in elf_group[2]][0] 
            groups_priority_sum += ord(badge) - (38 if badge.isupper() else 96)

        print(f"The sum of groups priority item values are: {str(groups_priority_sum)}")

if __name__ == "__main__":
    solve = Solution()
    # Answer to Part One
    solve.solution1()
    # Answer to Part Two
    solve.solution2()
