"""Module for triangle classification."""

def is_triangle(sides):
    """Check if the given sides can form a triangle."""
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    return side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1

def equilateral(sides):
    """Check if the triangle is equilateral."""
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    return is_triangle(sides) and side_1 == side_2 == side_3


def isosceles(sides):
    """Check if the triangle is isosceles."""
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    return is_triangle(sides) and (side_1 == side_2 or side_2 == side_3 or side_1 == side_3)


def scalene(sides):
    """Check if the triangle is scalene."""
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    return is_triangle(sides) and side_1 != side_2 and side_2 != side_3 and side_1 != side_3
