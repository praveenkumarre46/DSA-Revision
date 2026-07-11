from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        
        while queue:
            r, c, steps = queue.popleft()
            
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and [r, c] != entrance:
                return steps
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    maze[nr][nc] = "+"
                    queue.append((nr, nc, steps + 1))
                    
        return -1