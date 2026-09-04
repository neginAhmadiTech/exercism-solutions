CATEGORY_SCORES = [
    ("Royal Flush", 10),
    ("Straight Flush", 9),
    ("Four of a Kind", 8),
    ("Full House", 7),
    ("Flush", 6),
    ("Straight", 5),
    ("Three of a Kind", 4),
    ("Two Pair", 3),
    ("One Pair", 2),
    ("High Card", 1),
]
CARD_SCORES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def is_same_suit(hand):
    return all(word[-1] == hand[0][-1] for word in hand)


def remove_suit(hand):
    return [card.replace(card[-1], "") for card in hand]


def is_straight_flush(hand):

    return is_straight(hand) and is_same_suit(hand)


def is_four_of_a_kind(hand):

    cards = remove_suit(hand)

    return any(cards.count(card) == 4 for card in cards)


def is_full_house(hand):

    cards = remove_suit(hand)

    return len(set(cards)) == 2


def is_straight(hand):

    cards = remove_suit(hand)
    cards = [CARD_SCORES[card] for card in cards]
    cards_sorted = sorted(cards)

    if cards_sorted == [2, 3, 4, 5, 14]:
        cards_sorted[-1] = 1
        cards_sorted = sorted(cards_sorted)

    return cards_sorted == list(range(cards_sorted[0], cards_sorted[-1] + 1))


def is_three_of_a_kind(hand):
    cards = remove_suit(hand)

    return (
        cards.count(cards[0]) == 3
        or cards.count(cards[1]) == 3
        or cards.count(cards[2]) == 3
    )


def is_two_pair(hand):
    cards = remove_suit(hand)

    pairs = []
    for card in cards:
        if cards.count(card) == 2 and card not in pairs:
            pairs.append(card)

        if len(pairs) == 2:
            return True

    return False


def is_one_pair(hand):
    cards = remove_suit(hand)

    return any(cards.count(card) == 2 for card in cards)


def is_quadruple(hand, card):
    return hand.count(card) == 4


def is_triple(hand, card):
    return hand.count(card) == 3


def is_pair(hand, card):
    return hand.count(card) == 2


def is_kicker(hand, card):
    return hand.count(card) == 1


def highest_card(hands):

    highest_scores = []
    for hand in hands:
        hand_without_suits = remove_suit(hand.split(" "))

        if sorted(hand_without_suits, key=lambda score: CARD_SCORES[score]) == [
            "2",
            "3",
            "4",
            "5",
            "A",
        ]:
            max_card_value = 5
        else:
            max_card_value = max(CARD_SCORES[card] for card in hand_without_suits)

        highest_scores.append((max_card_value, hand))

    return [max(highest_scores, key=lambda score: score[0])[1]]


def highest_four_of_a_kind(hands):

    keys = []
    for hand in hands:

        hand_without_suits = remove_suit(hand.split(" "))
        quadruple = None
        kicker = None

        for card in hand_without_suits:
            if quadruple is None and is_quadruple(hand_without_suits, card):
                quadruple = CARD_SCORES[card]

            if kicker is None and is_kicker(hand_without_suits, card):
                kicker = CARD_SCORES[card]

        keys.append(((quadruple, kicker), hand))

    best_score = max(key for key, _ in keys)

    winning_hands = [hand for key, hand in keys if key == best_score]

    return winning_hands


def highest_full_house(hands):

    keys = []
    for hand in hands:

        hand_without_suits = remove_suit(hand.split(" "))
        triple = None
        pair = None

        for card in hand_without_suits:
            if triple is None and is_triple(hand_without_suits, card):
                triple = CARD_SCORES[card]

            if pair is None and is_pair(hand_without_suits, card):
                pair = CARD_SCORES[card]

        keys.append(((triple, pair), hand))

    best_score = max(key for key, _ in keys)

    winning_hands = [hand for key, hand in keys if key == best_score]

    return winning_hands


def highest_flush_and_high_card(hands):

    hands_without_suits = []
    for hand in hands:
        hands_without_suits.append((remove_suit(hand.split(" ")), hand))

    best_score = max(
        tuple(sorted([CARD_SCORES[card] for card in hand], reverse=True))
        for hand, _ in hands_without_suits
    )

    winning_hands = [
        original_hand
        for hand, original_hand in hands_without_suits
        if tuple(sorted([CARD_SCORES[card] for card in hand], reverse=True))
        == tuple(sorted(best_score, reverse=True))
    ]

    return winning_hands


def highest_three_of_a_kind(hands):

    keys = []
    for hand in hands:

        hand_without_suits = remove_suit(hand.split(" "))
        triple = None
        kickers = []

        for card in hand_without_suits:
            if triple is None and is_triple(hand_without_suits, card):
                triple = CARD_SCORES[card]

            if kickers.count(card) < 2 and is_kicker(hand_without_suits, card):
                kickers.append(CARD_SCORES[card])

        key = (triple, *sorted(kickers, reverse=True))
        keys.append((key, hand))

    best_score = max(key for key, _ in keys)

    winning_hands = [hand for key, hand in keys if key == best_score]

    return winning_hands


def highest_two_pair(hands):

    keys = []
    for hand in hands:

        hand_without_suits = remove_suit(hand.split(" "))
        pairs = []
        kicker = None

        for card in hand_without_suits:
            if kicker is None and is_kicker(hand_without_suits, card):
                kicker = CARD_SCORES[card]

            if pairs.count(card) < 2 and is_pair(hand_without_suits, card):
                pairs.append(CARD_SCORES[card])

        key = (*sorted(pairs, reverse=True), kicker)
        keys.append((key, hand))

    best_score = max(key for key, _ in keys)

    winning_hands = [hand for key, hand in keys if key == best_score]

    return winning_hands


def highest_one_pair(hands):
    keys = []
    for hand in hands:

        hand_without_suits = remove_suit(hand.split(" "))
        pair = None
        kickers = []

        for card in hand_without_suits:
            if pair is None and is_pair(hand_without_suits, card):
                pair = CARD_SCORES[card]

            if kickers.count(card) < 2 and is_kicker(hand_without_suits, card):
                kickers.append(CARD_SCORES[card])

        key = (pair, *sorted(kickers, reverse=True))
        keys.append((key, hand))

    best_score = max(key for key, _ in keys)

    winning_hands = [hand for key, hand in keys if key == best_score]

    return winning_hands


def best_hands(hands):

    scores = []

    for hand in hands:
        splitted_hand = hand.split(" ")

        if is_straight_flush(splitted_hand):
            scores.append((CATEGORY_SCORES[1], hand))

        elif is_four_of_a_kind(splitted_hand):
            scores.append((CATEGORY_SCORES[2], hand))

        elif is_full_house(splitted_hand):
            scores.append((CATEGORY_SCORES[3], hand))

        elif is_same_suit(splitted_hand):
            scores.append((CATEGORY_SCORES[4], hand))

        elif is_straight(splitted_hand):
            scores.append((CATEGORY_SCORES[5], hand))

        elif is_three_of_a_kind(splitted_hand):
            scores.append((CATEGORY_SCORES[6], hand))

        elif is_two_pair(splitted_hand):
            scores.append((CATEGORY_SCORES[7], hand))

        elif is_one_pair(splitted_hand):
            scores.append((CATEGORY_SCORES[8], hand))

        else:
            scores.append((CATEGORY_SCORES[9], hand))

    sorted_scores = sorted(scores, key=lambda score: score[0][1])
    max_hand_value = sorted_scores[-1][0][1]

    max_hands = []
    for value, hand in sorted_scores:
        if value[1] == max_hand_value:
            max_hands.append((value, hand))

    if len(max_hands) == 1:
        return [max_hands[0][1]]

    # --------- PART 2 ---------

    category = max_hands[0][0][0]

    match (category):
        case "Straight Flush":
            return highest_card([hand[1] for hand in max_hands])

        case "Four of a Kind":
            return highest_four_of_a_kind([hand[1] for hand in max_hands])

        case "Full House":
            return highest_full_house([hand[1] for hand in max_hands])

        case "Flush":
            return highest_flush_and_high_card([hand[1] for hand in max_hands])

        case "Straight":
            return highest_card([hand[1] for hand in max_hands])

        case "Three of a Kind":
            return highest_three_of_a_kind([hand[1] for hand in max_hands])

        case "Two Pair":
            return highest_two_pair([hand[1] for hand in max_hands])

        case "One Pair":
            return highest_one_pair([hand[1] for hand in max_hands])

        case "High Card":
            return highest_flush_and_high_card([hand[1] for hand in max_hands])
