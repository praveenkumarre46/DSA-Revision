# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inroot = TreeNode(-1)
        temp = inroot

        def dfs(node):
            nonlocal temp  
            if node == None:
                return
            
            dfs(node.left)
            
            node.left = None 
            temp.right = node
            temp = temp.right
            
            dfs(node.right)

        dfs(root)
        return inroot.right
        