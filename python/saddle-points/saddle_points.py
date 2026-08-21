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
        row_max_list = []

        row_max_list = [index for index, value in enumerate(row) if value == row_max]

        for row_max_index in row_max_list:
            col_list = [sub[row_max_index] for sub in matrix]
            col_min = min(col_list)

            if row_max == col_min:
                result.append({"row": row_index + 1, "column": row_max_index + 1})

    return result
