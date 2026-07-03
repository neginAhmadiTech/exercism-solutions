"""Module that calculates the points scored in a single toss of a Darts game 
"""
def score(x, y):
    """Function to calculate the points scored in a single toss of a Darts game 

    Args:
        x (int): x coordinate of the distance
        y (int): y coordinate of the distance

    Returns:
        int: correct score earned by a dart landing at that point. 
    """
    distance = ((x ** 2) + (y ** 2)) ** (1 / 2)
    points = 0

    if distance <= 1:
        points = 10
    elif distance <= 5:
        points = 5
    elif distance <= 10:
        points = 1

    return points
