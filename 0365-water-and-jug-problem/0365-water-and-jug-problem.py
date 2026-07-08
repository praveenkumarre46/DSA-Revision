class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
            
        queue = deque([[0, 0]])
        visited = set()
        visited.add((0, 0))
        
        while queue:
            j1, j2 = queue.popleft()
            
            if j1 + j2 == target:
                return True
                
            next_states = [
                (x, j2),
                (j1, y),
                (0, j2),
                (j1, 0),
                (j1 - min(j1, y - j2), j2 + min(j1, y - j2)),
                (j1 + min(j2, x - j1), j2 - min(j2, x - j1))
            ]
            
            for state in next_states:
                if state not in visited:
                    visited.add(state)
                    queue.append(state)
                    
        return False