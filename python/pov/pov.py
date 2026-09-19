from json import dumps

# from itertools import chain, imap


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def __iter__(self):

        # for node in chain(*imap(iter, self.children)):
        #     yield node
        yield from chain(*imap(iter, self.children))

        yield self.label

    def find_path(self, tree, target, result):

        result.append(tree)

        if target == tree.label:
            return result

        for child in tree.children:
            found = self.find_path(Tree(child.label, child.children), target, result)

            if found:
                return result

            if found is None:
                result.pop()

    def from_pov(self, from_node):

        from_node_path = self.find_path(self, from_node, result=[])

        if from_node_path is None:
            raise ValueError("Tree could not be reoriented")

        if len(from_node_path[0].children) == 0:
            return from_node_path[0]

        for index in range(0, len(from_node_path) - 1):

            from_node_path[index].children = [
                child
                for child in from_node_path[index].children
                if child.label != from_node_path[index + 1].label
            ]

        from_node_path = from_node_path[::-1]
        for index in range(0, len(from_node_path) - 1):
            from_node_path[index].children.append(from_node_path[index + 1])

        return from_node_path[0]

    def path_to(self, from_node, to_node):

        from_node_path = self.find_path(
            Tree(self.label, self.children), from_node, result=[]
        )

        to_node_path = self.find_path(
            Tree(self.label, self.children), to_node, result=[]
        )

        if to_node_path is None:
            raise ValueError("No path found")

        if from_node_path is None:
            raise ValueError("Tree could not be reoriented")

        # find intersection point
        i, j = 0, 0
        intersection = -1
        while i != len(from_node_path) and j != len(to_node_path):

            if i == j and from_node_path[i] == to_node_path[j]:
                i += 1
                j += 1
            else:
                intersection = j - 1
                break

        return [
            path.label
            for path in from_node_path[intersection : len(from_node_path)][::-1]
        ] + [path.label for path in to_node_path[intersection + 1 :]]
