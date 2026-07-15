from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        max_limit = max(x, max(forbidden)) + a + b
        
        queue = deque([(0, 0, False)])
        visited = {(0, False)}
        
        while queue:
            curr, jumps, was_backward = queue.popleft()
            
            if curr == x:
                return jumps
            
            next_forward = curr + a
            if next_forward <= max_limit and next_forward not in forbidden_set and (next_forward, False) not in visited:
                visited.add((next_forward, False))
                queue.append((next_forward, jumps + 1, False))
                
            if not was_backward:
                next_backward = curr - b
                if next_backward >= 0 and next_backward not in forbidden_set and (next_backward, True) not in visited:
                    visited.add((next_backward, True))
                    queue.append((next_backward, jumps + 1, True))
                    
        return -1