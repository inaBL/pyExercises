'''
Dice probability, Checkio:

Write a function that takes the number of dice, the number of sides per die and a target number and returns the probability of getting a total roll of exactly the target value.
The result should be given with four digits precision as ±0.0001.
For example, if you roll 2 six-sided dice, the probability of getting exactly a 3 is 2/36 or 5.56%, which you should return as ≈0.0556.

Input: Three arguments. The number of dice, the number of sides per die and the target number as integers.
Output: The probability of getting exactly target number on a single roll of the given dice as a float.

Preconditions:
1 ≤ dice_number ≤ 10
2 ≤ sides ≤ 20
0 ≤ target < 1000
'''

from itertools import combinations_with_replacement
from math import factorial
from collections import Counter


def probability(dice_number, sides, target):
    # trimmed combinations to curb processing time for outliers
    dice_combinations = combinations_with_replacement(range(1, sides + 1), dice_number)

    # favourable outcomes, calculating permutations only for fo
    fo = 0
    for die in dice_combinations:
        if sum(die) == target:
            c = Counter(die)
            perm = factorial(dice_number)
            for item in c:
                perm = perm/factorial(c[item])
            fo += perm

    return round(fo / (sides**dice_number), 4)


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    print(probability(3,6,7))
    assert probability(2, 6, 3) == 0.0556, "Basic example"
    assert probability(2, 6, 4) == 0.0833, "More points"
    assert probability(2, 6, 7) == 0.1667, "Maximum for two 6-sided dice"
    assert probability(2, 3, 5) == 0.2222, "Small dice"
    assert probability(2, 3, 7) == 0, "Never!"
    assert probability(3, 6, 7) == 0.0694, "Three dice"
    #assert probability(10, 10, 50) == 0.0375, "Many dice, many sides" <-- brute force lengthy wait, need to figure out better solution