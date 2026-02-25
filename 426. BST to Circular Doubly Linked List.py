def treeToDoublyList(root):
    if not root:
        return None

    def helper(node):
        """Returns (head, tail) of converted list"""
        if not node:
            return None, None

        left_head, left_tail = helper(node.left)
        right_head, right_tail = helper(node.right)

        # Connect left list to current node
        if left_tail:
            left_tail.right = node
            node.left = left_tail

        # Connect current node to right list
        if right_head:
            right_head.left = node
            node.right = right_head

        # Determine head and tail
        head = left_head or node
        tail = right_tail or node

        return head, tail

    head, tail = helper(root)

    # Make it circular
    head.left = tail
    tail.right = head

    return head