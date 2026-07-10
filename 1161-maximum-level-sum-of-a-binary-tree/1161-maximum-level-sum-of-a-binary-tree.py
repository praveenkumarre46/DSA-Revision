# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        glbsum=root.val
        glblvl=1
        lvl=0
        while queue:
            lvlsum=0
            for _ in range(len(queue)):
                node=queue.popleft()
                lvlsum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl+=1
            if lvlsum>glbsum:
                glbsum=lvlsum
                glblvl=lvl
        return glblvl

