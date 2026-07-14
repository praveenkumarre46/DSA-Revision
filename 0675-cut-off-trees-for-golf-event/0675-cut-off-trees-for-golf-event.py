from collections import deque
import heapq

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        rows = len(forest)
        cols = len(forest[0])
        pq = []
        
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] > 1:
                    heapq.heappush(pq, (forest[i][j], i, j))
                    
        def bfs(starti, startj, tari, tarj):
            pushed = set()
            queue = deque([(0, starti, startj)])
            pushed.add((starti, startj))
            
            while queue:
                steps, i, j = queue.popleft()
                if i == tari and j == tarj:
                    return steps
                    
                dirc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in dirc:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < rows and 0 <= nc < cols and forest[nr][nc] != 0 and (nr, nc) not in pushed:
                        queue.append((steps + 1, nr, nc))
                        pushed.add((nr, nc))
            return -1
            
        minsteps = 0
        previ, prevj = 0, 0
        
        for _ in range(len(pq)):
            height, i, j = heapq.heappop(pq)
            val = bfs(previ, prevj, i, j)
            if val == -1:
                return -1
            else:
                minsteps += val
                previ, prevj = i, j
                
        return minsteps