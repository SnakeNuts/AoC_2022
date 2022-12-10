#!/usr/bin/env python3
"""
Advent of Code 2022 - Day 3 - part 2
"""

__author__ = "Alex Crouzen"
__version__ = "0.1.0"
__license__ = "MIT"


def get_item_priority(item: list) -> int:
    item_value = 0
    if ord(item[0]) >= 97:
        item_value = ord(item[0]) - 96
    else:
        item_value = ord(item[0]) - 38

    return item_value


def main():
    """ Main entry point of the app """
    total_priority = 0
    with open("day3_data.txt") as data:
        while True:
            elves = list()
            # 3 elves per group
            finished = False
            for counter in range(3):
                elf = data.readline()
                if elf == '':
                    finished = True
                    break
                elves.append(elf.strip())
            if finished:
                break

            # find common item
            common_1_2 = list(set(elves[0]).intersection(elves[1]))
            common_with_3 = list(set(common_1_2).intersection(elves[2]))
            total_priority += get_item_priority(common_with_3)

    print(total_priority)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
