"""Module  to find anagrams of a word in a given list of words
"""
def find_anagrams(word, candidates):
    """Function to find anagrams of a word in a 
    given list of words

    Args:
        word (str): given word
        candidates (list): given list of words

    Returns:
        list: list of words that are the anagram of the given word
    """
    result = []
    word = word.lower()

    for candidate in candidates:
        candidate_lower = candidate.lower()

        if candidate_lower == word:
            continue

        if len(candidate_lower) != len(word):
            continue

        sorted_word = str(sorted(list(word)))
        sorted_candidate = str(sorted(list(candidate_lower)))

        if sorted_word == sorted_candidate:
            result.append(candidate)

    return result
