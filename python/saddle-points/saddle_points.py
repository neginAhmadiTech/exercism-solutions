def is_regular(matrix):
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            return False
    return True


def saddle_points(matrix):

    if not matrix:
        return []

    if not is_regular(matrix):
        raise ValueError("irregular matrix")

    result = []
    for row_index, row in enumerate(matrix):
        row_max = max(row)

        max_indices = [index for index, value in enumerate(row) if value == row_max]

        for column_index in max_indices:
            column = [row[column_index] for row in matrix]
            column_min = min(column)

            if row_max == column_min:
                result.append({"row": row_index + 1, "column": column_index + 1})

    return result
