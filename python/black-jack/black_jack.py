"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
FACED_CARDS = "JQK"
ACE_CARD = "A"

def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """


    result = 0

    if card in FACED_CARDS:
        result = 10
    elif card == ACE_CARD:
        result = 1
    elif 2 <= int(card) <= 10:
        result = int(card)

    return result


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    result = ""

    if card_one_value < card_two_value:
        result = card_two
    elif card_two_value < card_one_value:
        result = card_one
    else:
        result = (card_one, card_two)

    return result


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    if ACE_CARD in (card_one, card_two):
        return 1

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    result = 0

    if card_one_value + card_two_value + 11 <= 21:
        result = 11
    else:
        result = 1

    return result




def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    # blackjack_cards = "AJQK"
    result = False

    if (card_one in ACE_CARD and card_two not in ACE_CARD) or (card_two in ACE_CARD and card_one not in ACE_CARD):
        result = True

    return result

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    result = False

    if card_one_value == card_two_value:
        result = True

    return result


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    double_down_points = [9, 10, 11]
    total_value = card_one_value + card_two_value
    result = False

    if total_value in double_down_points:
        result = True

    return result
