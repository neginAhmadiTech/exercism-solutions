LETTER_SCORES = {
    1: "aeioulnrst",
    2: "dg",
    3: "bcmp",
    4: "fhvwy",
    5: "k",
    8: "jx",
    10: "qz",
}


def score(word):
    word = word.lower()
    result = 0

    for letter in word:
        for point, letters in LETTER_SCORES.items():
            if letter in letters:
                result += point
                break

    return result
