from collections import defaultdict


class School:
    def __init__(self):
        self.school = defaultdict(list)
        self.added_list = []

    def _check_duplicate_name(self, name):
        for students in self.school.values():
            if name in students:
                return True
        return False

    def add_student(self, name, grade):

        if self._check_duplicate_name(name):
            self.added_list.append(False)
            return

        self.school[grade].append(name)
        self.added_list.append(True)

    def roster(self):
        result = []
        for item in sorted(self.school.items()):
            for student in sorted(item[1]):
                result.append(student)

        return result

    def grade(self, grade_number):
        return sorted(self.school.get(grade_number, []))

    def added(self):
        return self.added_list
