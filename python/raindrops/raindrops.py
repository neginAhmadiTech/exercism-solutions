"""Module including one function that gets a number and converts it
to its corresponding raindrop sounds
"""
def convert(number):
    """Function to convert a number into its corresponding raindrop sounds.

    Args:
        number (int): given number for analyzing

    Returns:
        string: a string that is the result of analyzing the number and turning
        it into its corresponding raindrop sounds.
    """
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "":
        return str(number)
    return result
