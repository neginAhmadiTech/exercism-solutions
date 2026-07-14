"""This module provides a function to count the number of eggs in a display.
"""
def egg_count(display_value):
    """Count the number of eggs in a display.

    Args:
        display_value (int): The number of eggs to count.

    Returns:
        int: The total number of eggs.
    """

    number_of_eggs = 0

    if display_value == 0:
        return number_of_eggs


    while display_value > 1:
        print(display_value % 2)
        if display_value % 2 == 1:
            number_of_eggs += 1

        display_value = display_value // 2

    return number_of_eggs + 1
