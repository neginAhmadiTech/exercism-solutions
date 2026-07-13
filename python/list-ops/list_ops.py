"""Module to implement built-in functions of lists
"""
def append(list1, list2):
    """Redefining built-in 'append'.

    Args:
        list1 (list): list1 given
        list2 (list): list2 to add to the list1

    Returns:
        list: the combination of two lists
    """
    return list1 + list2


def concat(lists):
    """Redefining built-in 'concat'.

    Args:
        lists (list): given list of lists

    Returns:
        list: the combination of lists
    """
    result = []
    for given_list in lists:
        result = result + given_list
    return result


def filter(function, list):
    """Filter the given list using the provided function.

    Args:
        function (callable): The function to apply to each item
        list (list): The list to filter

    Returns:
        list: A new list containing only the items for which the function returns True
    """
    result = []
    for item in list:
        if function(item):
            result.append(item)

    return result


def length(list):
    """Redefining built-in 'len'.

    Args:
        list (list): The list whose length is to be determined

    Returns:
        int: The length of the list
    """
    length_count = 0
    for _ in list:
        length_count = length_count + 1

    return length_count



def map(function, list):
    """Redefining built-in 'map'.

    Args:
        function (callable): The function to apply to each item
        list (list): The list to map

    Returns:
        list: A new list containing the results of applying the function to each item
    """
    result = []

    for item in list:
        result.append(function(item))

    return result


def foldl(function, list, initial):
    """Redefining built-in 'foldl'.

    Args:
        function (callable): The function to apply to each item
        list (list): The list to fold
        initial (_type_): The initial value

    Returns:
        _type_: The folded value
    """

    result = initial
    for item in list:
        result = function(result, item)

    return result


def foldr(function, list, initial):
    """Redefining built-in 'foldr'.

    Args:
        function (callable): The function to apply to each item
        list (list): The list to fold
        initial (_type_): The initial value

    Returns:
        _type_: The folded value
    """

    list = reverse(list)
    result = initial
    for item in list:
        result = function(result, item)

    return result



def reverse(list):
    """Redefining built-in 'reverse'

    Args:
        list (list): given list

    Returns:
        list: reversed list
    """
    return list[::-1]
