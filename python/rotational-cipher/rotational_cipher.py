"""Module for implementing the rotational cipher algorithm
"""
def rotate(text, key):
    """Function to calculate the rotated text of a given text based on rotational cipher

    Args:
        text (str): The text to be rotated
        key (int): The key for the rotational cipher

    Returns:
        str: The rotated text
    """
    rotated_text = []
    for char in text:
        if char.isalpha():
            if char.islower():
                rotated_text.append(chr((ord(char) - ord("a") + key) % 26 + ord("a")))
            else:
                rotated_text.append(chr((ord(char) - ord("A") + key) % 26 + ord("A")))
        else:
            rotated_text.append(char)

    return "".join(rotated_text)
