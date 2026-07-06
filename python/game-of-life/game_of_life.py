
"""Module for implementing Conway's Game of Life.
"""
def number_of_alive_neighbors(matrix, cell_row, cell_col):
    """Function to count the number of alive neighbors around a specified cell.

    Args:
        matrix (list): Grid of cells represented as a list of lists,
        where 1 represents a live cell and 0 represents a dead cell.
        cell_row (int): Row index of the cell for which to count alive neighbors.
        cell_col (int): Column index of the cell for which to count alive neighbors.

    Returns:
        int: The number of alive neighbors around the specified cell.
    """
    count = 0
    rows = len(matrix)
    columns = len(matrix[0])

    if cell_col < columns - 1 and matrix[cell_row][cell_col + 1] == 1:
        count = count + 1
    if cell_col < columns - 1 and cell_row < rows - 1 and matrix[cell_row + 1][cell_col + 1] == 1:
        count = count + 1
    if cell_row < rows - 1 and matrix[cell_row + 1][cell_col] == 1:
        count = count + 1
    if cell_col > 0 and cell_row < rows - 1 and matrix[cell_row + 1][cell_col - 1] == 1:
        count = count + 1
    if cell_col > 0 and matrix[cell_row][cell_col - 1] == 1:
        count = count + 1
    if cell_col > 0 and cell_row > 0 and matrix[cell_row - 1][cell_col - 1] == 1:
        count = count + 1
    if cell_row > 0 and matrix[cell_row - 1][cell_col] == 1:
        count = count + 1
    if cell_col < columns - 1 and cell_row > 0 and matrix[cell_row - 1][cell_col + 1] == 1:
        count = count + 1

    return count


def apply_rule_two(matrix, row, column):
    """Function to apply rule two

    Args:
        matrix (list): Grid of cells represented as a list of lists, 
        where 1 represents a live cell and 0 represents a dead cell.
        row (int): Row index of the cell to apply the rule to.
        column (int): Column index of the cell to apply the rule to.

    Returns:
        bool: True if the cell should be alive in the next generation, False otherwise.
    """

    cell = matrix[row][column]
    result = False

    if cell == 0 and number_of_alive_neighbors(matrix, row, column) == 3:
        result = True

    return result

def apply_rule_one(matrix, row, column):
    """Function to apply rule one

    Args:
        matrix (list): Grid of cells represented as a list of lists,
        where 1 represents a live cell and 0 represents a dead cell.
        row (int): Row index of the cell to apply the rule to.
        column (int): Column index of the cell to apply the rule to.

    Returns:
        bool: True if the cell should be alive in the next generation, False otherwise.
    """

    cell = matrix[row][column]
    result = False

    if cell == 1 and (number_of_alive_neighbors(matrix, row, column) == 2 or number_of_alive_neighbors(matrix, row, column) == 3):
        result = True

    return result


def tick(matrix):
    """Function that takes a matrix and returns a new matrix with the next generation
    of cells based on the rules of Conway's Game of Life.

    Args:
        matrix (list): Grid of cells represented as a list of lists,
        where 1 represents a live cell and 0 represents a dead cell.

    Returns:
        list: Grid of cells represented as a list of lists,
        where 1 represents a live cell and 0 represents a dead cell.
    """
    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])

    converted_matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):

            if apply_rule_one(matrix, row_index, column_index):
                converted_matrix[row_index][column_index] = 1
            elif apply_rule_two(matrix, row_index, column_index):
                converted_matrix[row_index][column_index] = 1
            else:
                converted_matrix[row_index][column_index] = 0


    return converted_matrix
