"""Module to convert a given plain text
    into a ciphered encoded text
"""
def cipher_text(plain_text):
    """Function to convert a given plain text
    into a ciphered encoded text

    Args:
        plain_text (str): given plain text

    Returns:
        str: converted ciphered text
    """

    plain_text_cleaned = ""
    plain_text = plain_text.lower()

    for char in plain_text:
        if char.isalnum():
            plain_text_cleaned += char

    if len(plain_text_cleaned) < 2:
        return plain_text_cleaned

    text_length = len(plain_text_cleaned)
    square_root = text_length ** (1 / 2)
    row = 0
    column = 0

    if int(square_root) == square_root:
        row = column = int(square_root)
    else:
        row = int(square_root)
        column = int(square_root) + 1


    if row * column > text_length:
        row += 1

    rectangle = [plain_text_cleaned[index: index + column] for index in range(0, len(plain_text_cleaned), column)]

    for index, rectangle_row in enumerate(rectangle):
        if len(rectangle_row) < column:
            rectangle[index] += (" " * (column - len(rectangle_row)))


    result = []
    for col_index in range(len(rectangle[0])):

        ciphered = ""
        for row in rectangle:
            ciphered += row[col_index]

        result.append(ciphered)
        ciphered = ""

    return " ".join(result)
