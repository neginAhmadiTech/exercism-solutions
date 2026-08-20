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


def correct_frequency(dice, number_types, frequency):
    dice_set = set(dice)
    if len(dice_set) not in number_types:
        return False

    number_1_frequency = len([val for val in dice if val == list(dice_set)[0]])
    if number_1_frequency not in frequency:
        return False

    return True


def score_big_straight(dice):

    if set(dice) == set(range(2, 7)):
        return 30

    return 0


def score_little_straight(dice):

    if set(dice) == set(range(1, 6)):
        return 30

    return 0


def score_four_of_a_kind(dice):
    if not correct_frequency(dice, [1, 2], [1, 4, 5]):
        return 0

    dice_set = set(dice)
    number_frequency = len([val for val in dice if val == list(dice_set)[0]])

    if number_frequency == 1:
        number_frequency = len([val for val in dice if val == list(dice_set)[1]])
        return number_frequency * list(dice_set)[1]

    return 4 * list(dice_set)[0]


def score_full_house(dice):

    if not correct_frequency(dice, [2], [2, 3]):
        return 0

    return sum(dice)


def score_numbers(dice, number):
    number_frequency = len([val for val in dice if val == number])

    return number * number_frequency


def score(dice, category):
    result = 0

    match (category):
        case value if value in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
            result = score_numbers(dice, category)

        case value if value == FULL_HOUSE:
            result = score_full_house(dice)

        case value if value == FOUR_OF_A_KIND:
            result = score_four_of_a_kind(dice)

        case value if value == LITTLE_STRAIGHT:
            result = score_little_straight(dice)

        case value if value == BIG_STRAIGHT:
            result = score_big_straight(dice)

        case value if value == CHOICE:
            result = sum(dice)

        case value if value == YACHT:
            if correct_frequency(dice, [1], [5]):
                result = 50

    return result
