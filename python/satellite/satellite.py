def tree_from_traversals(preorder, inorder):

    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")

    if not preorder:
        return {}

    root = preorder[0]
    root_index = inorder.index(root)

    left_side_inorder = inorder[:root_index]
    right_side_inorder = inorder[root_index + 1 :]

    left_side_preorder = preorder[1 : root_index + 1]
    right_side_preorder = preorder[root_index + 1 :]

    return {
        "v": root,
        "l": (tree_from_traversals(left_side_preorder, left_side_inorder)),
        "r": (tree_from_traversals(right_side_preorder, right_side_inorder)),
    }
