"""Module for resistor color label with tolerance
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

COLORS_TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}




def convert_large_values(number):
    """Converting the large values into a specific format

    Args:
        number (int): given number to convert

    Returns:
        str: the label after converting
    """
    ohms_weight = 0
    label_value = ""

    while number >= 1000:
        number = number / 1000
        ohms_weight = ohms_weight + 1

    if number.is_integer():
        number = int(number)

    if ohms_weight == 0:
        label_value = f"{number} ohms"
    elif ohms_weight == 1:
        label_value = f"{number} kiloohms"
    elif ohms_weight == 2:
        label_value = f"{number} megaohms"
    elif ohms_weight == 3:
        label_value = f"{number} gigaohms"

    return label_value


def adding_tolerance(label_value, tolerance):
    """Function to add tolerance to the label

    Args:
        label_value (str): existing label value
        tolerance (str): tolerance of the resistor

    Returns:
        str: new label after adding tolerance
    """

    tolerance_value = COLORS_TOLERANCE.get(tolerance)
    label_value = label_value + f" ±{tolerance_value}%"

    return label_value


def resistor_label(colors):
    """Function to convert the band colors

    Args:
        colors (list): given list of resistor colors

    Returns:
        str: the converted label
    """

    number = 0
    label_value = ""
    colors_length = len(colors)

    if colors_length == 1:
        label_value = f"{COLORS.index(colors[0])} ohms"

    elif colors_length == 4:
        band_1 = str(COLORS.index(colors[0]))
        band_2 = str(COLORS.index(colors[1]))
        band_3 = COLORS.index(colors[2])
        band_4 = colors[3]

        number = int(band_1 + band_2) * (10 ** band_3)
        label_value = convert_large_values(number)
        label_value = adding_tolerance(label_value, band_4)

    elif colors_length == 5:
        band_1 = str(COLORS.index(colors[0]))
        band_2 = str(COLORS.index(colors[1]))
        band_3 = str(COLORS.index(colors[2]))
        band_4 = COLORS.index(colors[3])
        band_5 = colors[4]

        number = int(band_1 + band_2 + band_3) * (10 ** band_4)
        label_value = convert_large_values(number)
        label_value = adding_tolerance(label_value, band_5)

    return label_value
