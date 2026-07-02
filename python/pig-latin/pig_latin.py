"""Module for translating text into Pig Latin."""

VOWELS = ("a", "e", "i", "o", "u")
CONSONANTS = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")


def translate(text):
    """Translate a sentence into Pig Latin."""
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word):
    """Translate a single word into Pig Latin."""
    if starts_with_vowel_sound(word):
        return word + "ay"

    index = qu_index(word)
    if index is not None:
        return word[index + 2:] + word[:index + 2] + "ay"

    index = y_index(word)
    if index is not None:
        return word[index:] + word[:index] + "ay"

    index = first_vowel_index(word)
    return word[index:] + word[:index] + "ay"


def starts_with_vowel_sound(word):
    """Return True if the word starts with a vowel sound."""
    return (
        word.startswith(VOWELS)
        or word.startswith("xr")
        or word.startswith("yt")
    )


def first_vowel_index(word):
    """Return the index of the first vowel."""
    for index, char in enumerate(word):
        if char in VOWELS:
            return index
    return -1


def qu_index(word):
    """Return the index of 'qu' when it belongs to the initial consonant cluster."""
    index = word.find("qu")
    if index == -1:
        return None

    if word.startswith("qu"):
        return index

    if all(char in CONSONANTS for char in word[:index]):
        return index

    return None


def y_index(word):
    """Return the index of 'y' when it acts as the first vowel."""
    if word.startswith("y"):
        return None

    index = word.find("y")
    if index == -1:
        return None

    if all(char in CONSONANTS for char in word[:index]):
        return index

    return None
