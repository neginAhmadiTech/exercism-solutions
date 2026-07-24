"""Module to count the number of neighbor flowers for each specific
    cell and replace the number with the cell data
"""

def number_of_neighbors_flowers(garden, cell_row, cell_col):
    """Function to count the number of neighbors with flowers around a specified cell.

    Args:
        matrix (list): Grid of cells represented as a list of lists
        cell_row (int): Row index of the cell for which to count neighbors with flowers.
        cell_col (int): Column index of the cell for which to count neighbors with flowers.

    Returns:
        int: The number of neighbors with flowers around the specified cell.
    """
    count = 0
    rows = len(garden)
    columns = len(garden[0])

    if cell_col < columns - 1 and garden[cell_row][cell_col + 1] == "*":
        count = count + 1
    if cell_col < columns - 1 and cell_row < rows - 1 and garden[cell_row + 1][cell_col + 1] == "*":
        count = count + 1
    if cell_row < rows - 1 and garden[cell_row + 1][cell_col] == "*":
        count = count + 1
    if cell_col > 0 and cell_row < rows - 1 and garden[cell_row + 1][cell_col - 1] == "*":
        count = count + 1
    if cell_col > 0 and garden[cell_row][cell_col - 1] == "*":
        count = count + 1
    if cell_col > 0 and cell_row > 0 and garden[cell_row - 1][cell_col - 1] == "*":
        count = count + 1
    if cell_row > 0 and garden[cell_row - 1][cell_col] == "*":
        count = count + 1
    if cell_col < columns - 1 and cell_row > 0 and garden[cell_row - 1][cell_col + 1] == "*":
        count = count + 1

    if count == 0:
        return " "

    return str(count)

def annotate(garden):
    """Count the number of neighbor flowers for each specific
    cell and replace the number with the cell data

    Args:
        garden (list): The list of the strings of the garden

    Raises:
        ValueError: Raise a ValueError if we have invalid data 
        for the cells
        ValueError: Raise a ValueError if the length of the
        rows are not equal

    Returns:
        list: The result list after counting the neighbor flowers
    """
    garden = [list(row) for row in garden]

    if len(garden) > 0:
        row_length = len(garden[0])

    for row_index, row in enumerate(garden):

        if row_length != len(row):
            raise ValueError("The board is invalid with current input.")

        for column_index, column in enumerate(row):

            if column not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")

            if column == " ":
                flowers_count = number_of_neighbors_flowers(garden, row_index, column_index)
                garden[row_index][column_index] = flowers_count

    return ["".join(row) for row in garden]
