"""Module for converting a number from an input_base to a given output_base
"""
def rebase(input_base, digits, output_base):
    """Function to convert a number from an input_base to a given output_base

    Args:
        input_base (int): Given input base 
        digits (list): Given list of numbers to convert
        output_base (int): Given output base to convert to

    Raises:
        ValueError: Raises error if given input_base is < 2
        ValueError: Raises error if given output_base is < 2
        ValueError: Raises error if one of the digits of the number is < 0 or >= input_base

    Returns:
        list: Converted list to the output_base
    """

    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    base_ten = 0
    for index, digit in enumerate(digits):

        if input_base == 10:
            base_ten = int("".join(str(digit) for digit in digits))
            break

        base_ten = base_ten + ((input_base ** ((len(digits) - 1) - index)) * digit)


    output_base_converted = []
    while base_ten >= output_base:
        remainder = base_ten % output_base
        base_ten = base_ten // output_base
        output_base_converted.append(remainder)
    output_base_converted.append(base_ten)

    output_base_converted.reverse()

    return output_base_converted
