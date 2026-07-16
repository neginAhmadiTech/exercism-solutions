"""Module to finds the magic windows in a given string containing numbers
    with a given magic window length
"""
def slices(series, length):
    """Finds the magic windows in a given string containing numbers
    with a given magic window length

    Args:
        series (str): The string containing the number
        length (int): The length of the magic window

    Raises:
        ValueError: Raises if the slice length is zero
        ValueError: Raises if the slice length is negative
        ValueError: Raises if the series is empty
        ValueError: Raises if the slice length is greater than series length

    Returns:
        list: The list of the magic windows
    """

    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    result = []

    for index in range(len(series) - length + 1):
        result.append(series[index:index+length])

    return result
