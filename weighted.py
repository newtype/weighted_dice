import random

# key: name of side, value: weight of side
dice_sides = {
    "movie" : 1,
    "lecture": 3,
    "reading": 5,
    }

def roll(dice_sides):
    """ Randomly pick a side, respecting each side's weight """
    expanded_sides = [
        weighted_side
        for side, weight in dice_sides.items()
        for weighted_side in [side] * weight
    ]
    return random.choice(expanded_sides)


def main():
    print("Rolling dice...")
    result = roll(dice_sides)
    print("Result:", result)

if __name__ == '__main__':
    main()
