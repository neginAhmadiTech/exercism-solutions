"""Module for resistor color label
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

def adding_third_color(number, third_color):
    """Function to convert the third color of the resistor

    Args:
        number (int): given number with two first colors converted
        third_color (str): the third color of the resistor

    Returns:
        int: the number after adding the third color
    """


    if third_color == "brown":
        number = number * 10
    elif third_color == "red":
        number = number * 100
    elif third_color == "orange":
        number = number * 1000
    elif third_color == "yellow":
        number = number * 10000
    elif third_color == "green":
        number = number * 100000
    elif third_color == "blue":
        number = number * 1000000
    elif third_color == "violet":
        number = number * 10000000
    elif third_color == "grey":
        number = number * 100000000
    elif third_color == "white":
        number = number * 1000000000

    return number



def label(colors):
    """Function to translate the resistor colors into ohms

    Args:
        colors (list): given list of resistor colors

    Returns:
        str: the label of the resistor
    """

    number = int(str(COLORS.index(colors[0])) + str(COLORS.index(colors[1])))
    label_value = ""

    number = adding_third_color(number, colors[2])

    ohms_weight = 0
    while number > 1000:
        number = number // 1000
        ohms_weight = ohms_weight + 1


    if ohms_weight == 0:
        label_value = f"{number} ohms"
    elif ohms_weight == 1:
        label_value = f"{number} kiloohms"
    elif ohms_weight == 2:
        label_value = f"{number} megaohms"
    elif ohms_weight == 3:
        label_value = f"{number} gigaohms"    

    return label_value
