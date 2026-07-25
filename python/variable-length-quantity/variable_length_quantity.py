"""Module to encode and decode list of
numbers based on VLQ
"""
def encode(numbers):
    """Encode list of hex numbers
    based on VLQ encoding algorithm

    Args:
        numbers (list): The given list of numbers

    Returns:
        list: Encoded list
    """

    result = []
    for number in numbers:
        number_binary = bin(number)[2:]
        binary_str = str(number_binary)
        seven_bit_groups = list(reversed([binary_str[max(i-7,0):i] for i in range(len(binary_str),0,-7)]))

        if len(seven_bit_groups[0]) < 7:
            seven_bit_groups[0] = ((7-len(seven_bit_groups[0])) * "0") + seven_bit_groups[0]

        for index, value in enumerate(seven_bit_groups):

            if index == len(seven_bit_groups) - 1:
                seven_bit_groups[index] = "0" + value
                result.append((int(seven_bit_groups[index], 2)))
                continue

            seven_bit_groups[index] = "1" + value
            result.append((int(seven_bit_groups[index], 2)))

    return result


def decode(bytes_):
    """Decode list of hex numbers
    based on VLQ decoding algorithm

    Args:
        bytes_ (list): The given list of numbers

    Raises:
        ValueError: Raises if the last byte doesn't end

    Returns:
        list: Decoded list
    """

    result = []
    flag_bits = []
    for index, byte in enumerate(bytes_):

        number_binary = bin(byte)[2:]
        binary_str = str(number_binary)

        if len(binary_str) < 8:
            flag_bits.append("0")
            result.append((((8-len(binary_str)) * "0") + binary_str)[1:])
            continue

        flag_bits.append(binary_str[0])
        result.append(binary_str[1:])

    final_numbers = []
    final_number = ""
    for index, item in enumerate(result):
        if index == len(result) - 1:

            if flag_bits[index] == "1":
                raise ValueError("incomplete sequence")

        final_number += item
        if flag_bits[index] == "0":
            final_numbers.append(int(final_number, 2))
            final_number = ""

    return final_numbers
