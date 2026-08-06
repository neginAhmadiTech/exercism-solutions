"""Module for encoding and decoding messages using the rail fence cipher.
"""

def get_rail(index, rails):
    """Function to get the rail position for a given index.

    Args:
        index (int): Index of the letter in the message
        rails (int): Number of rails for the cipher

    Returns:
        int: Rail position for the given index
    """
    rail_position = index % (2 * (rails - 1))

    if rail_position >= rails:
        rail_position = (2 * (rails - 1)) - rail_position

    return rail_position


def encode(message, rails):
    """Function to encode a message using the rail fence cipher.

    Args:
        message (str): Given message to encode
        rails (int): Number of rails for the cipher

    Returns:
        str: Encoded message
    """
    cipher_list = ["" for _ in range(rails)]
    message_list = list(message)

    for index, letter in enumerate(message_list):
        rail_position = get_rail(index, rails)
        cipher_list[rail_position] += letter

    return "".join(cipher_list)


def decode(encoded_message, rails):

    """Function to decode a message using the rail fence cipher.

    Args:
        encoded_message (str): Given encoded message to decode
        rails (int): Number of rails for the cipher

    Returns:
        str: Decoded message
    """

    # phase 1: Count how many letters each rail gets
    rail_count = [0] * rails
    for letter_position in range(len(encoded_message)):
        rail_position = get_rail(letter_position, rails)
        rail_count[rail_position] += 1

    # phase 2: Split the ciphertext
    rail_text = [[]] * rails
    encoded_message_filtered = encoded_message
    for rail in range(rails):
        rail_text[rail] = list(encoded_message_filtered[0: rail_count[rail]])
        encoded_message_filtered = encoded_message_filtered[rail_count[rail]:]

    # phase 3: build the result
    result = ""
    for letter_position in range(len(encoded_message)):
        rail_position = get_rail(letter_position, rails)
        result += rail_text[rail_position].pop(0)

    return result
