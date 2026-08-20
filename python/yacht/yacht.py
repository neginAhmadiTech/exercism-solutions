YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def correct_frequency(dice, frequency):
    dice_set = set(dice)
    if len(dice_set) != 2:
        return False

    first_number_frequency = dice.count(list(dice_set)[0])
    if first_number_frequency not in frequency:
        return False

    return True


def score_yacht(dice):
    for item in dice:
        if dice.count(item) == 5:
            return 50

    return 0


def score_big_straight(dice):

    if set(dice) == set(range(2, 7)):
        return 30

    return 0


def score_little_straight(dice):

    if set(dice) == set(range(1, 6)):
        return 30

    return 0


def score_four_of_a_kind(dice):
    for item in dice:
        if dice.count(item) == 4 or dice.count(item) == 5:
            return 4 * item

    return 0


def score_full_house(dice):

    if not correct_frequency(dice, [2, 3]):
        return 0

    return sum(dice)


def score_numbers(dice, number):
    number_frequency = dice.count(number)

    return number * number_frequency


def score(dice, category):

    match (category):
        case value if value in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
            return score_numbers(dice, category)

        case value if value == FULL_HOUSE:
            return score_full_house(dice)

        case value if value == FOUR_OF_A_KIND:
            return score_four_of_a_kind(dice)

        case value if value == LITTLE_STRAIGHT:
            return score_little_straight(dice)

        case value if value == BIG_STRAIGHT:
            return score_big_straight(dice)

        case value if value == CHOICE:
            return sum(dice)

        case value if value == YACHT:
            return score_yacht(dice)
