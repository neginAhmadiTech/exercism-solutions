"""Module for generating a thank you message for a customer based on their position in line.
"""
def line_up(name, number):
    """Function to generate a thank you message for a customer based on their position in line.

    Args:
        name (str): The name of the customer.
        number (int): The position of the customer in line.

    Returns:
        str: A thank you message for the customer.
    """
    number_suffix = ""

    if str(number).endswith("11") or str(number).endswith("12") or str(number).endswith("13"):
        number_suffix = "th"
        thanks_sentence = f"{name}, you are the {number}{number_suffix} customer we serve today. Thank you!"
        return thanks_sentence

    if str(number).endswith("1"):
        number_suffix = "st"
    elif str(number).endswith("2"):
        number_suffix = "nd"
    elif str(number).endswith("3"):
        number_suffix = "rd"
    else:
        number_suffix = "th"

    thanks_sentence = f"{name}, you are the {number}{number_suffix} customer we serve today. Thank you!"
    return thanks_sentence
