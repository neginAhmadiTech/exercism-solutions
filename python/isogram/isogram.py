"""Module for checking if a phrase is an isogram or not.
"""
def is_isogram(phrase):
    """Check if the given phrase is isogram or not. 

    Args:
        phrase (str): The phrase to check

    Returns:
        bool: True if the phrase is an isogram, False otherwise
    """
    result = True
    filtered_phrase = phrase.lower()
    for letter in filtered_phrase:
        if letter.isalpha() and filtered_phrase.count(letter) > 1:
            result = False
    return result
