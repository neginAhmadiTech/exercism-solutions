from copy import deepcopy


class Zipper:
    def __init__(self, tree):
        self.tree = deepcopy(tree)
        self.focus = self.tree
        self.path = []

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.focus["value"]

    def set_value(self, value):
        self.focus["value"] = value
        return self

    def left(self):

        if self.focus["left"] is not None:
            self.path.append(self.focus)
            self.focus = self.focus["left"]
            return self

    def set_left(self, left):

        self.focus["left"] = left
        return self

    def right(self):

        if self.focus["right"] is not None:
            self.path.append(self.focus)
            self.focus = self.focus["right"]
            return self

    def set_right(self, right):

        self.focus["right"] = right
        return self

    def up(self):

        if not self.path:
            return None

        self.focus = self.path.pop()
        return self

    def to_tree(self):
        return self.tree
