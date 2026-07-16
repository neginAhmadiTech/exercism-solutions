"""Module for finding prime factors of a given number
"""

# def is_prime(value):
#     """Checks if a number is prime

#     Args:
#         value (int): Given number to check if it's prime

#     Returns:
#         bool: True if the number is prime, False otherwise
#     """

#     for item in range(2, value):
#         if value % item == 0:
#             return False
#     return True


def factors(value):
    """Finds all prime factors of a given number

    Args:
        value (int): Given number to find prime factors for

    Returns:
        list: A list of all prime factors of the given number
    """
    result = []
    number = value

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            result.append(divisor)
            number //= divisor
        else:
            if divisor == 2:
                divisor = 3
            else:
                divisor += 2

    if number > 1:
        result.append(number)

    return result
