
"""Module for resistor color code
"""
COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white"
]

def color_code(color):
    """Function to return the number of given color in 
    the resistor colors

    Args:
        color (str): The color for which to find the code

    Returns:
        int: The code for the given color
    """
    return COLORS.index(color)


def colors():
    """Function to return the list of resistor colors

    Returns:
        list: The list of resistor colors
    """
    return COLORS
