"""Module for encoding and decoding text using the Atbash cipher.
The Atbash cipher is a simple substitution cipher that replaces each letter
with its corresponding letter in the reverse alphabet. 
"""
def encode(plain_text):
    """Encodes the given plain text using the Atbash cipher.

    Args:
        plain_text (str): The text to encode

    Returns:
        str: The encoded text
    """
    plain_text = plain_text.lower()

    encoded_text = ""

    for char in plain_text:

        if char.isnumeric():
            encoded_text += char

        if char.isalpha():
            encoded = 96 + (123 - ord(char))
            encoded_text += chr(encoded)


    result = ""
    for index in range(0, len(encoded_text), 5):
        result += encoded_text[index: index + 5] + " "

    return result.strip()


def decode(ciphered_text):
    """Decodes the given ciphered text using the Atbash cipher.

    Args:
        ciphered_text (str): The text to decode

    Returns:
        str: The decoded text
    """

    ciphered_text = ciphered_text.lower()

    decoded_text = ""

    for char in ciphered_text:

        if char.isnumeric():
            decoded_text += char

        if char.isalpha():
            decoded = 96 + (123 - ord(char))
            decoded_text += chr(decoded)

    return decoded_text
