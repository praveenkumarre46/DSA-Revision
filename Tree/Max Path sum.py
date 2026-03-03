# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')

        def rec(node):
            nonlocal maxsum
            if not node:
                return 0

            left = max(rec(node.left), 0)
            right = max(rec(node.right), 0)

            maxsum = max(maxsum, node.val + left + right)

            return node.val + max(left, right)

        rec(root)
        return maxsum

        