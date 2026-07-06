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

def value(colors):
    """Function to calculate the number of the resistor
    based on the given colors

    Args:
        colors (list): the color given to calculate the number

    Returns:
        int: the number of the resistor
    """
    return int(str(COLORS.index(colors[0])) + str(COLORS.index(colors[1])))
