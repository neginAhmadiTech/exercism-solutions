"""Module to convert a given sentence into another string 
containing the first chars of each word uppercased and joined together
"""
def abbreviate(words):
    """Gets a sentence and returns the first chars of each word
    uppercased and joined together

    Args:
        words (str): the sentence given

    Returns:
        str: the string with first chars uppercased
    """

    words = words.replace("-", " ")

    words_without_punctuation = ""
    for letter in words:
        if not letter.isalpha() and not letter.isspace():
            punctuation_removed = letter.replace(letter, "")
            words_without_punctuation += punctuation_removed
        else:
            words_without_punctuation += letter

    words_without_punctuation = words_without_punctuation.title()
    words_list = words_without_punctuation.split(" ")

    result = ""
    for word in words_list:
        word.strip()
        if len(word) != 0:
            result += word[0]

    return result
