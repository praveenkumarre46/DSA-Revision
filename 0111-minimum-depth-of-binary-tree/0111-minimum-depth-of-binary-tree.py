# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lt = self.minDepth(root.left)
        rt = self.minDepth(root.right)
        
        if not root.left or not root.right:
            return max(lt, rt) + 1
        
        return min(lt, rt) + 1