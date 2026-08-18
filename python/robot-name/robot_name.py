import random
import string


class Robot:

    used_names = set()

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name is None:
            self._name = self.generate_name()
            self.used_names.add(self._name)

        return self._name

    def generate_name(self):
        letters = "".join(random.choices(string.ascii_uppercase, k=2))
        numbers = "".join(random.choices(string.digits, k=3))

        return letters + numbers

    def reset(self):
        self.used_names.remove(self._name)

        while True:
            if self.generate_name() not in self.used_names:
                self._name = self.generate_name()
                break
