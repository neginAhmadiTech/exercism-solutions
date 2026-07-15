"""Module for creating a diamond pattern with letters of the alphabet.
"""
def rows(letter):
    """Create a diamond pattern with the given letter at the widest point.

    Args:
        letter (str): Given letter to create diamond

    Returns:
        list[str]: List of strings representing the rows of the diamond
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(letter)
    rows_length = index * 2 + 1
    middle_index = index


    result = []
    for row_index in range(rows_length):
        distance = abs(middle_index - row_index)
        letter_index = index - distance
        leading_spaces = distance * " "

        row = ""
        if letter_index == 0:
            row += leading_spaces + alphabet[letter_index] + leading_spaces
        else:
            inside_spaces = (letter_index * 2 - 1) * " "
            row_letter = alphabet[letter_index]
            row += leading_spaces + row_letter + inside_spaces + row_letter + leading_spaces

        result.append(row)
    return result
