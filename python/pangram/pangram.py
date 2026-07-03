"""Module to check if a given sentence is a pangram or not.
A pangram is a sentence that contains every letter of the alphabet at least once.
"""
def is_pangram(sentence):
    """Check if a given sentence is pangram or not. 
    A pangram is a sentence that contains every letter of the alphabet at least once.

    Args:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = False
    helper_alphabet_array = [False] * 26
    sentence_alphabet_letters = 0

    for letter in sentence:
        if letter in alphabet:
            alphabet_index = alphabet.index(letter)
            helper_alphabet_array[alphabet_index] = True


    for item in helper_alphabet_array:
        # print(item)
        if item is True:
            sentence_alphabet_letters = sentence_alphabet_letters + 1


    if sentence_alphabet_letters == 26:
        result = True

    return result
