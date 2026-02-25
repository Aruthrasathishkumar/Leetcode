def filterBST(root, min_val, max_val):
    if not root:
        return None

    # Prune left subtree if current value too small
    if root.val < min_val:
        return filterBST(root.right, min_val, max_val)

    # Prune right subtree if current value too large
    if root.val > max_val:
        return filterBST(root.left, min_val, max_val)

    # Node is in range, recursively filter children
    new_node = TreeNode(root.val)
    new_node.left = filterBST(root.left, min_val, max_val)
    new_node.right = filterBST(root.right, min_val, max_val)

    return new_node