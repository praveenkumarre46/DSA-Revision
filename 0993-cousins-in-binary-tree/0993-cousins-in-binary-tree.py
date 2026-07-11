class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
            
        queue = deque([root])
        
        while queue:
            xfound = False
            yfound = False
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.val == x:
                    xfound = True
                if node.val == y:
                    yfound = True
                    
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                       (node.left.val == y and node.right.val == x):
                        return False
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if xfound and yfound:
                return True
                
        return False