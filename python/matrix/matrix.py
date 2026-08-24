class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        self._convert_matrix(matrix_string)

    def _convert_matrix(self, matrix_string):
        rows_str = matrix_string.splitlines()

        for row in rows_str:
            columns = row.split(" ")
            columns = [int(column) for column in columns]
            self.matrix.append(columns)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
