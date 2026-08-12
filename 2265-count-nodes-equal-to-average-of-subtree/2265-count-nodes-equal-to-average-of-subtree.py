# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

  def averageOfSubtree(self, root: TreeNode) -> int:
    count = 0

    def dfs(node):
      nonlocal count
      if not node:
        return (0, 0)

      ltsum, ln = dfs(node.left)
      rtsum, rn = dfs(node.right)

      total_sum = ltsum + rtsum + node.val
      total_count = ln + rn + 1

      if total_sum // total_count == node.val:
        count += 1

      return (total_sum, total_count)

    dfs(root)
    return count