"""
This module provides a function to determine if a given year is a leap year.
A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
"""
def leap_year(year):
    """
    Determines if a given year is a leap year.
    
    A year is a leap year if it is divisible by 4, but not by 100,
    unless it is also divisible by 400.
    
    Args:
        year (int): The year to check.
        
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
