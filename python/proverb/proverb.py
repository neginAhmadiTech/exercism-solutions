def proverb(*args, qualifier):
    result = []
    first_card = ""

    if len(args) == 0:
        return result

    if len(args) > 0:
        first_card = args[0]

    while len(args) > 1:
        first, *args = args
        sentence = f"For want of a {first} the {args[0]} was lost."
        result.append(sentence)

    final_sentence = (
        f"And all for the want of a {qualifier+" " if qualifier else ""}{first_card}."
    )

    result.append(final_sentence)

    return result
