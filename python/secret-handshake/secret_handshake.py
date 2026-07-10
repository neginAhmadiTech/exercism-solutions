"""Module to convert the given binary code into a list of commands
"""
def commands(binary_str):
    """Function to convert the given binary code
    into a list of commands

    Args:
        binary_str (str): given binary code

    Returns:
        list: translated list of commands
    """
    commands_list = []

    if binary_str[-1] == "1":
        commands_list.append("wink")
    if binary_str[-2] == "1":
        commands_list.append("double blink")
    if binary_str[-3] == "1":
        commands_list.append("close your eyes")
    if binary_str[-4] == "1":
        commands_list.append("jump")

    if binary_str[-5] == "1":
        commands_list.reverse()

    return commands_list
