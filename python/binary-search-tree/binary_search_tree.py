class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree_data = tree_data
        self.tree = None

    def _insert_data(self, root, data):

        if data <= root.data:
            if root.left is None:
                root.left = TreeNode(data, None, None)
            else:
                self._insert_data(root.left, data)
        else:
            if root.right is None:
                root.right = TreeNode(data, None, None)
            else:
                self._insert_data(root.right, data)

        return root

    def data(self):
        tree_data = self.tree_data.copy()

        if self.tree is None:
            self.tree = TreeNode(tree_data.pop(0), None, None)

        for data in tree_data:
            self.tree = self._insert_data(self.tree, data)

        return self.tree

    # inorder dfs
    def _traverse_tree(self, tree, sorted_tree):

        if tree is not None:
            self._traverse_tree(tree.left, sorted_tree)
            sorted_tree.append(tree.data)
            self._traverse_tree(tree.right, sorted_tree)

        return sorted_tree

    def sorted_data(self):
        return self._traverse_tree(self.data(), [])
