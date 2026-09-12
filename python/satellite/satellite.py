def tree_from_traversals(preorder, inorder):

    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    if len(preorder) == len(inorder) == 0:
        return {}

    root = preorder[0]

    inorder_str = "".join(inorder)
    splitted_inorder_str = inorder_str.split(root)
    left_side_inorder = list(splitted_inorder_str[0])
    right_side_inorder = list(splitted_inorder_str[1])

    left_side_preorder = [node for node in preorder if node in left_side_inorder]
    right_side_preorder = [node for node in preorder if node in right_side_inorder]

    return {
        "v": root,
        "l": (tree_from_traversals(left_side_preorder, left_side_inorder)),
        "r": (tree_from_traversals(right_side_preorder, right_side_inorder)),
    }
