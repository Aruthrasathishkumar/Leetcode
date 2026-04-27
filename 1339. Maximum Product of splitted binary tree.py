# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subtree_sums = []

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total = node.val + left_sum + right_sum
            subtree_sums.append(total)

            return total

        total_sum = dfs(root)

        max_product = 0

        for subtree_sum in subtree_sums:
            remaining_sum = total_sum - subtree_sum
            product = subtree_sum * remaining_sum
            max_product = max(max_product, product)

        return max_product % MOD
