DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def next_cell_full(matrix, row, column, direction_index):
    return (
        matrix[row + DIRECTIONS[direction_index][0]][
            column + DIRECTIONS[direction_index][1]
        ]
        is not None
    )


def right_not_allowed(direction, row, size):
    return direction == (1, 0) and row + 1 == size


def bottom_not_allowed(direction, column, size):
    return direction == (0, 1) and column + 1 == size


def left_not_allowed(direction, column):
    return direction == (0, -1) and column - 1 == -1


def spiral_matrix(size):

    if size == 0:
        return []

    matrix = [[None] * size for _ in range(size)]

    direction = DIRECTIONS[0]
    cell_number = 2
    matrix[0][0] = 1
    row = 0
    column = 1
    while cell_number <= size**2:
        direction_index = DIRECTIONS.index(direction)

        if (
            right_not_allowed(direction, row, size)
            or bottom_not_allowed(direction, column, size)
            or left_not_allowed(direction, column)
            or next_cell_full(matrix, row, column, direction_index)
        ):

            direction = DIRECTIONS[(direction_index + 1) % 4]

        matrix[row][column] = cell_number
        cell_number += 1
        row += direction[0]
        column += direction[1]

    return matrix
