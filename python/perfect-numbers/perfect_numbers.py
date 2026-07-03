"""Module to calculate if a number is equal to the sum of its factors
"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    result = 0
    sum_of_factors = 0

    for item in range(1, number):
        if number % item == 0:
            sum_of_factors = sum_of_factors + item

    if sum_of_factors == number:
        result = "perfect"
    elif sum_of_factors > number:
        result = "abundant"
    else:
        result = "deficient"

    return result
