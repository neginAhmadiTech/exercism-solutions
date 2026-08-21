from collections import defaultdict


class School:
    def __init__(self):
        self.students_by_grade = defaultdict(list)
        self.students = set()
        self.added_list = []

    def add_student(self, name, grade):

        if name in self.students:
            self.added_list.append(False)
            return

        self.students_by_grade[grade].append(name)
        self.students.add(name)
        self.added_list.append(True)

    def roster(self):
        result = []
        for grade, students in sorted(self.students_by_grade.items()):
            for student in sorted(students):
                result.append(student)

        return result

    def grade(self, grade_number):
        return sorted(self.students_by_grade.get(grade_number, []))

    def added(self):
        return self.added_list
