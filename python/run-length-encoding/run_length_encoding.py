"""Module for encoding and decoding given text
"""
def decode(string):
    """Decodes a given string and returns the decoded text

    Args:
        string (str): Text to decode

    Returns:
        str: The decoded text
    """
    result = ""

    multiplier = ""
    for index, letter in enumerate(string):

        if letter.isnumeric():
            multiplier += letter
        else:
            left_letter = string[index - 1]

            if string[0] == letter or left_letter.isalpha() or left_letter.isspace():
                result += letter
                multiplier = ""
                continue

            result += letter * int(multiplier)
            multiplier = ""

    return result



def encode(string):
    """Encodes a given string and returns the encoded text

    Args:
        string (str): Text to encode

    Returns:
        str: The encoded text
    """

    letter_count = 0
    result = ""
    for index, letter in enumerate(string):
        if index != (len(string) - 1) and letter == string[index + 1]:
            letter_count += 1
        else:
            letter_count += 1

            if letter_count == 1:
                result += letter
            else:
                result += str(letter_count) + letter

            letter_count = 0

    return result
