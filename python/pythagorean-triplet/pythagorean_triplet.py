import math


def triplets_with_sum(number):
    triplets = []
    for third in range(int(number / 2) - 1, int((math.sqrt(2) - 1) * number), -1):
        formula = math.sqrt(third**2 - number**2 + 2 * number * third)
        if formula == int(formula):
            triplets.append(
                [
                    int((number - third - formula) / 2),
                    int((number - third + formula) / 2),
                    third,
                ]
            )
    return triplets
