from typing import List
import collections

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked_set = {tuple(b) for b in blocked}
        MAX_VISITS = 20000 
        
        def bfs(start, end):
            queue = collections.deque([tuple(start)])
            visited = {tuple(start)}
            
            while queue:
                r, c = queue.popleft()
                
                if list((r, c)) == end:
                    return True
                
                if len(visited) > MAX_VISITS:
                    return True
                    
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < 10**6 and 0 <= nc < 10**6:
                        if (nr, nc) not in visited and (nr, nc) not in blocked_set:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            
            return False
            
        return bfs(source, target) and bfs(target, source)