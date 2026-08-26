ALLERGY_ITEMS = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
]


class Allergies:

    def __init__(self, score):
        self.score = score
        self.items = []

    def allergic_to(self, item):
        return (self.score & (2 ** ALLERGY_ITEMS.index(item))) != 0

    @property
    def lst(self):
        for index, allergy_item in enumerate(ALLERGY_ITEMS):
            if self.score & (2**index) != 0:
                self.items.append(allergy_item)
                self.score -= 2**index

        return self.items
