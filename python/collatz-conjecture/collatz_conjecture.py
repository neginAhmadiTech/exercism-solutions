
"""Calculating the count of steps until the number is 1
"""
def steps(number):
    """Function to calculate the steps of Collatz Conjecture

    Raises:
        ValueError: if we have zero or negative numbers

    Returns:
        int: the count of steps until the number reaches to 1
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps_count = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

        steps_count = steps_count + 1

    return steps_count
