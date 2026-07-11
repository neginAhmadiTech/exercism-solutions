"""Module for calculating the Hamming distance between two DNA strands.
"""
def distance(strand_a, strand_b):
    """Calculate the Hamming distance between two DNA strands.

    Args:
        strand_a (str): The first DNA strand.
        strand_b (str): The second DNA strand.

    Raises:
        ValueError: If the strands are not of equal length.

    Returns:
        int: The Hamming distance between the two strands.
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    counter = 0
    for index, value in enumerate(strand_a):
        if value != strand_b[index]:
            counter = counter + 1

    return counter
