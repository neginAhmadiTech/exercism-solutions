class CustomSet:
    def __init__(self, elements=None):
        if elements is None:
            elements = []

        self.elements = []
        for element in elements:
            if element not in self.elements:
                self.elements.append(element)

    @property
    def length(self):
        return len(self.elements)

    def isempty(self):
        return self.length == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(element in other for element in self.elements)

    def isdisjoint(self, other):
        return len([element for element in self.elements if element in other]) == 0

    def __eq__(self, other):
        return len(self.elements) == len(other.elements) and self.issubset(other)

    def add(self, element):

        if element not in self.elements:
            self.elements.append(element)

        return self

    def intersection(self, other):
        return CustomSet([element for element in self.elements if element in other])

    def __sub__(self, other):
        return CustomSet([element for element in self.elements if element not in other])

    def __add__(self, other):
        return CustomSet(self.elements + other.elements)
