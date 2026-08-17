def proverb(*args, qualifier):

    if not args:
        return []

    result = []
    first_card = args[0]

    while len(args) > 1:
        first, *args = args
        second = args[0]
        sentence = f"For want of a {first} the {second} was lost."
        result.append(sentence)

    qualified_card = f"{qualifier} " if qualifier else ""
    final_sentence = f"And all for the want of a {qualified_card}{first_card}."

    result.append(final_sentence)

    return result
