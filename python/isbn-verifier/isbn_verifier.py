
"""Module for validating ISBN-10 numbers."""
def find_last_char_value(last_char):
    """Find the value of the last char in a given isbn

    Args:
        last_char (str): The last character of the ISBN

    Returns:
        int: The value of the last character
    """
    result = False
    if last_char == "X":
        result = 10
    elif last_char.isdigit():
        result = int(last_char)

    return result


def calculate_sum_of_weights(isbn, last_char):
    """Calculate the sum of weights for a given isbn

    Args:
        isbn (str): The ISBN string to validate
        last_char (int): The value of the last character

    Returns:
        int: The sum of weights
    """
    sum_of_weights = 0

    for index, number in enumerate(isbn):
        number_weight = int(number) * (10 - index)
        sum_of_weights = sum_of_weights + number_weight

    return sum_of_weights + last_char


def is_valid(isbn):
    """Check is the given isbn is valid

    Args:
        isbn (str): The ISBN string to validate

    Returns:
        bool: True if the ISBN is valid, False otherwise
    """
    isbn = isbn.replace("-", "")
    last_char = ""
    result = False

    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit():
        return False

    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False

    last_char = find_last_char_value(isbn[len(isbn) - 1])
    isbn = list(isbn[:len(isbn) - 1])

    sum_of_weights = calculate_sum_of_weights(isbn, last_char)

    if sum_of_weights % 11 == 0:
        result = True

    return result
