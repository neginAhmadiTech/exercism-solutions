"""Module to flat a list of iterables and return the flatten array
"""
def flatten(iterable):
    """Flat a list of iterables and return the flatten array

    Args:
        iterable (list): given list of iterables

    Returns:
        list: the result list after flatting
    """
    result = []
    if isinstance(iterable, list):
        for item in iterable:
            result.extend(flatten(item))
    else:
        if iterable is not None:
            result.append(iterable)
    return result
