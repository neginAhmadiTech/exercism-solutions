"""Module for checking if brackets in a string are properly paired.
"""
def is_paired(input_string):
    """Check if all brackets in a string are properly paired.

    Args:
        input_string (str): The string to check for paired brackets.

    Returns:
        bool: True if all brackets are properly paired, False otherwise.
    """

    result = True

    opening_brackets = []
    closing_brackets = []

    for char in input_string:
        if char in "({[":
            opening_brackets.append(char)

        if char in ")}]":

            last_bracket = ""
            if len(opening_brackets) != 0:
                last_bracket = opening_brackets.pop()

            closing_brackets.append(char)

            pairs = {
                ")": "(",
                "}": "{",
                "]": "[",
            }

            if last_bracket == pairs.get(char):
                closing_brackets.pop()
            else:
                result = False


    if len(closing_brackets) != 0 or len(opening_brackets) != 0:
        result = False

    return result
