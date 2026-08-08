"""Module to change the format of letters 
    and points in a given legacy code
"""
def transform(legacy_data):
    """Function to change the format of letters 
    and points in a given legacy code

    Args:
        legacy_data (dict): Given legacy data

    Returns:
        dict: Changed data
    """

    result = {}

    for key, value in legacy_data.items():
        for letter in value:
            result[letter.lower()] = key

    return result
