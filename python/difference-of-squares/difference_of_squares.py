"""Module to calculate the difference of squares for a given number.
"""
def square_of_sum(number):
    """Calculate the square of the sum of the first 'number' natural numbers.

    Args:
        number (int): A positive integer

    Returns:
        int: The square of the sum of the first 'number' natural numbers
    """
    sum_of_nums = 0
    for num in range(number):
        sum_of_nums = sum_of_nums + (num + 1)

    square = sum_of_nums ** 2

    return square



def sum_of_squares(number):
    """Calculate the sum of the squares of the first 'number' natural numbers.

    Args:
        number (int): A positive integer

    Returns:
        int: The sum of the squares of the first 'number' natural numbers
    """
    squares_sum = 0
    for num in range(number):
        squares_sum = squares_sum + ((num + 1) ** 2)

    return squares_sum


def difference_of_squares(number):
    """Caclculate the absolute difference between 
    the sum of the squares and the square of sum

    Args:
        number (int): A positive integer

    Returns:
        int: The absolute difference between the sum of the squares and the square of the sum
    """
    return abs(sum_of_squares(number) - square_of_sum(number))
