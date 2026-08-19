BOARD_SIZE = 8


class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self._validate_position()

    def _validate_position(self):
        if self.row < 0:
            raise ValueError("row not positive")

        if self.row >= BOARD_SIZE:
            raise ValueError("row not on board")

        if self.column < 0:
            raise ValueError("column not positive")

        if self.column >= BOARD_SIZE:
            raise ValueError("column not on board")

    def same_row(self, another_queen):
        return self.row == another_queen.row

    def same_column(self, another_queen):
        return self.column == another_queen.column

    def same_diagonal(self, another_queen):
        return abs(self.column - another_queen.column) == abs(
            self.row - another_queen.row
        )

    def can_attack(self, another_queen):

        if self.same_row(another_queen) and self.same_column(another_queen):
            raise ValueError("Invalid queen position: both queens in the same square")

        return (
            self.same_row(another_queen)
            or self.same_column(another_queen)
            or self.same_diagonal(another_queen)
        )
