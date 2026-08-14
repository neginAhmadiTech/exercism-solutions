"""Module for using timedelta to add
1 gigasecond to a specific datetime"""

from datetime import timedelta


def add(moment):
    """Adding 1 gigasecond to a given datetime
    and returns the new datetime

    Args:
        moment (datetime): The given time

    Returns:
        datetime: converted time after adding 1 gigasecond
    """
    return moment + timedelta(seconds=1000000000)
