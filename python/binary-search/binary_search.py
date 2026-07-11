"""Module for performing binary search on a sorted list.
"""
def find(search_list, value):
    """Performs a binary search on a sorted list to find the index of a given value.

    Args:
        search_list (list): The sorted list to search.
        value (int): The value to find.

    Raises:
        ValueError: If the value is not found in the list.

    Returns:
        int: The index of the value if found.
    """

    if len(search_list) == 0:
        raise ValueError("value not in array")

    mid = len(search_list) // 2
    if search_list[mid] == value:
        return mid

    if search_list[mid] > value:
        return find(search_list[:mid], value)

    return (mid + 1) + find(search_list[mid + 1:], value)
