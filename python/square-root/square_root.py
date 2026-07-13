"""Module for calculating the square root of a number.
"""
def square_root(number):
    """Find the square root of a given number. (Newton's (Heron's) Method)

    Args:
        number (int): The number to find the square root of

    Returns:
        int: The square root of the number
    """

    guess = number

    while 1:
        new_guess = (guess + number / guess) / 2

        if new_guess == guess:
            return guess

        guess = new_guess
