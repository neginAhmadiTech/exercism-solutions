"""Module to find the n-th prime among prime numbers
"""
def is_prime(number):
    """Checks if a number is prime

    Args:
        value (int): Given number to check if it's prime

    Returns:
        bool: True if the number is prime, False otherwise
    """

    limit = int(number ** 0.5)

    for item in range(2, limit + 1):
        if number % item == 0:
            return False

    return True


def prime(number):
    """Find the n-th prime among prime numbers

    Args:
        number (int): The given number

    Raises:
        ValueError: Raises if the given number is less than 1

    Returns:
        int: n-th prime number
    """
    if number < 1:
        raise ValueError("there is no zeroth prime")

    if number == 1:
        return 2

    prime_numbers = []
    counter = 3
    result = 1
    while 1:
        if counter % 2 != 0:
            if is_prime(counter):
                prime_numbers.append(counter)

                if number == len(prime_numbers):
                    result = prime_numbers[number - 2]
                    break

        counter += 1

    return result
