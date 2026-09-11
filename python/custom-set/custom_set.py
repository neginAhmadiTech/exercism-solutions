class CustomSet:
    def __init__(self, elements=[]):
        self.length = len(elements)
        self.elements = []

        for element in elements:
            if element not in self.elements:
                self.elements.append(element)

    def isempty(self):
        return self.length == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return (
            len([element for element in self.elements if element in other.elements])
            == self.length
        )

    def isdisjoint(self, other):
        return (
            len([element for element in self.elements if element in other.elements])
            == 0
        )

    def __eq__(self, other):
        return sorted(other.elements) == sorted(self.elements)

    def add(self, element):

        if element not in self.elements:
            self.elements.append(element)
            self.length += 1

        return self

    def intersection(self, other):
        return CustomSet(
            [element for element in self.elements if element in other.elements]
        )

    def __sub__(self, other):
        return CustomSet(
            [element for element in self.elements if element not in other.elements]
        )

    def __add__(self, other):
        return CustomSet(self.elements + other.elements)
