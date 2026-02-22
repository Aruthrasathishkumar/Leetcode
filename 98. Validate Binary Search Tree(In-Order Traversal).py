# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(root):
    prev = float('-inf')

    def inorder(node):
        nonlocal prev
        if not node:
            return True

        if not inorder(node.left):
            return False

        if node.val <= prev:
            return False

        prev = node.val

        return inorder(node.right)

    return inorder(root)