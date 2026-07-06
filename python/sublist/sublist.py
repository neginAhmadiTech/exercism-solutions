"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

"""Module to check if a list is a sublist, superlist, equal or unequal to another list.
"""
def sublist(list_one, list_two):
    """Function to check if one list is a sublist, superlist, equal or unequal to another list.

    Args:
        list_one (list): The first list to compare.
        list_two (list): The second list to compare.

    Returns:
        str: The relationship between the two lists.
    """
    result = ""
    list_one_str = "|" + "||".join(str(item) for item in list_one) + "|"
    list_two_str = "|" + "||".join(str(item) for item in list_two) + "|"

    if list_one_str == list_two_str:
        result = EQUAL
    elif list_one_str in list_two_str:
        result = SUBLIST
    elif list_two_str in list_one_str:
        result = SUPERLIST
    else:
        result = UNEQUAL

    return result
