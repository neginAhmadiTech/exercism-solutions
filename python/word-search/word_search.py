class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def _is_outside_puzzle(self, row, column):

        print("inside function: ", row, column)

        return (
            row < 0
            or column < 0
            or row > len(self.puzzle) - 1
            or column > len(self.puzzle[0]) - 1
        )

    def search(self, word):

        start_points = []

        for row_index, row in enumerate(self.puzzle):
            for column_index, column in enumerate(row):
                if column == word[0]:
                    start_points.append(Point(row_index, column_index))

        for point in start_points:
            for direction in DIRECTIONS:
                current_row = point.x
                current_column = point.y

                word_matches = True

                for letter in word[1:]:
                    current_row += direction[0]
                    current_column += direction[1]

                    if self._is_outside_puzzle(current_row, current_column):
                        word_matches = False
                        break

                    if self.puzzle[current_row][current_column] != letter:
                        word_matches = False
                        break

                if word_matches:
                    return (Point(point.y, point.x), Point(current_column, current_row))

        return None
