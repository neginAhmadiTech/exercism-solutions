DEFAULT_STUDENTS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]

PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


class Garden:

    def __init__(self, diagram, students=None):

        self.rows = diagram.splitlines()

        if students is None:
            self.students = DEFAULT_STUDENTS
            return

        self.students = sorted(students)

    def plants(self, student):
        start_index = self.students.index(student) * 2
        cups = (
            self.rows[0][start_index : start_index + 2]
            + self.rows[1][start_index : start_index + 2]
        )

        return [PLANTS[plant] for plant in cups]
