"""Calculate the sum of the multiplies of a given multiply
list numbers until they get to a limited number
"""


def sum_of_multiples(limit, multiples):
    """Calculate the sum of the multiplies of a given multiply
    list numbers until they get to a limited number

    Args:
        limit (int): The limitation number
        multiples (list[int]): The list of multiplies numbers

    Returns:
        int: Sum of the multiplies
    """

    multiples_set = set()

    for multiply in multiples:

        if multiply == 0:
            multiples_set.add(multiply)
            continue

        multiples_list = list(range(multiply, limit, multiply))

        multiples_set.update(set(multiples_list))

    return sum(multiples_set)
