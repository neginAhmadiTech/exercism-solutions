
"""Module for calculating the largest and smallest palindromes
which are products of two numbers within a given range.
"""
def is_palindrome(number):
    """Calculates whether a number is a palindrome.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    
    number_str = str(number)
    return number_str == number_str[::-1]
    

def factors_of(number, min_factor, max_factor):
    """Finds all factor pairs of a number within a given range.

    Args:
        number (int): The number to find factors for.
        min_factor (int): The minimum factor to consider.
        max_factor (int): The maximum factor to consider.

    Returns:
        list: A list of factor pairs.
    """
    
    factors = []
    for candidate in range(min_factor, int(number**0.5) + 1):
        if number % candidate == 0:
            remainder = number // candidate
            if min_factor <= remainder <= max_factor and candidate <= remainder:
                factors.append([candidate, remainder])

    return factors

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    product = (None, [])
    candidate = max_factor * max_factor
    
    while candidate >= min_factor * min_factor:
        if is_palindrome(candidate):
            if factors_of(candidate, min_factor, max_factor):
                product = (candidate, factors_of(candidate, min_factor, max_factor))
                break
        candidate -= 1

    return product


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    
    product = (None, [])
    candidate = min_factor * min_factor
    
    while candidate <= max_factor * max_factor:
        if is_palindrome(candidate):
            if factors_of(candidate, min_factor, max_factor):
                product = (candidate, factors_of(candidate, min_factor, max_factor))
                break
        candidate += 1

    return product
