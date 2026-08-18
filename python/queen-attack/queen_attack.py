class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.validation()

    def validation(self):
        if self.row < 0:
            raise ValueError("row not positive")

        if self.row > 7:
            raise ValueError("row not on board")

        if self.column < 0:
            raise ValueError("column not positive")

        if self.column > 7:
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

        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        return (
            self.same_row(another_queen)
            or self.same_column(another_queen)
            or self.same_diagonal(another_queen)
        )
