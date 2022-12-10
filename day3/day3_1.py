#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    with open("day3_data.txt") as data:
        priority_sum = 0
        for line in data.readlines():
            compartment_1 = line.strip()[:len(line)//2]
            compartment_2 = line.strip()[len(line)//2:]
            for item in compartment_1:
                if item in compartment_2:
                    item_value = 0
                    if ord(item) >= 97:
                        item_value = ord(item) - 96
                    else:
                        item_value = ord(item) - 38
                    print(item, item_value)
                    priority_sum += item_value
                    break
        print(priority_sum)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()