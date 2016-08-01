""" Rolls a weighted dice with custom sides that you define.
"""

import sys
import random
import json


def roll(dice_sides):
    """ Randomly pick a side, respecting each side's weight """
    expanded_sides = [
        weighted_side
        for side, weight in dice_sides.items()
        for weighted_side in [side] * weight
    ]
    return random.choice(expanded_sides)


def main():
    try:
        sides = json.load(open(sys.argv[1]))
    except:
        print("gimme a json file name as the first arg")
    print(roll(sides))

if __name__ == '__main__':
    main()
