ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

SPECIAL_LINES = {
    "fly": "I don't know why she swallowed the fly. Perhaps she'll die.",
    "spider": "It wriggled and jiggled and tickled inside her.",
    "bird": "How absurd to swallow a bird!",
    "cat": "Imagine that, to swallow a cat!",
    "dog": "What a hog, to swallow a dog!",
    "goat": "Just opened her throat and swallowed a goat!",
    "cow": "I don't know how she swallowed a cow!",
    "horse": "She's dead, of course!",
}


def build_verse(verse_number):

    animal = ANIMALS[verse_number]
    first_line = f"I know an old lady who swallowed a {animal}."
    result = []
    result.append(first_line)
    result.append(SPECIAL_LINES[animal])

    if animal == "horse":
        return result

    for item in range(verse_number, 0, -1):
        verse = f"She swallowed the {ANIMALS[item]} to catch the {ANIMALS[item-1]}."

        if item == 2:
            verse = verse.replace(".", "")
            special_line = SPECIAL_LINES[ANIMALS[item - 1]]
            special_line = special_line.replace("It", "")
            special_verse = f"{verse} that{special_line}"
            result.append(special_verse)
            continue

        result.append(verse)

    if verse_number > 0:
        result.append(SPECIAL_LINES[ANIMALS[0]])

    return result


def recite(start_verse, end_verse):

    result = []

    for verse_number in range(start_verse - 1, end_verse):

        result += build_verse(verse_number)

        if verse_number == end_verse - 1:
            continue

        result.append("")

    return result
