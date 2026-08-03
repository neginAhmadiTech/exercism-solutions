"""Module to recite the lyrics to that popular children's repetitive song: Ten Green Bottles.
"""
NUMBERS = {
    0: "no",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
}

def recite(start, take=1):
    """Recite the lyrics to that popular children's repetitive song: Ten Green Bottles.

    Args:
        start (int): The starting verse
        take (int, int): How many steps go backward. Defaults to 1.

    Returns:
        list: The recited text
    """
    
    final_text = []
    sentence_3 = "And if one green bottle should accidentally fall,"
    
    while take > 0:
        sentence_1 = f"{NUMBERS[start]} green bottles hanging on the wall,"
        sentence_2 = f"{NUMBERS[start]} green bottles hanging on the wall,"
        sentence_4 = f"There'll be {NUMBERS[start - 1].lower()} green bottles hanging on the wall."
        
        if start == 1:
            sentence_1 = sentence_1.replace("bottles", "bottle")
            sentence_2 = sentence_2.replace("bottles", "bottle")
        elif start == 2:
            sentence_4 = sentence_4.replace("bottles", "bottle")
    
        final_text.append(sentence_1)
        final_text.append(sentence_2)
        final_text.append(sentence_3)
        final_text.append(sentence_4)
        
        if take > 1:
            final_text.append("")

        take -= 1
        start -= 1

    return final_text
