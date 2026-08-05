"""Module for counting the occurrences of each word in a sentence.
"""
def count_words(sentence):
    """Function to count the occurrences of each word in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """

    sentence = sentence.lower()
    words = []

    for letter in sentence:
        if letter in "_.,:;!@#$%^&*()[]{}\"`~":
            sentence = sentence.replace(letter, " ")

    for word in sentence.split():

        filtered_word = word.strip("'")

        if filtered_word:
            words.append(filtered_word)

    word_count = {}
    for word in words:
        word_count.setdefault(word, words.count(word))
    return word_count
