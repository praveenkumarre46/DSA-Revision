class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows=len(isWater)
        cols=len(isWater[0])
        queue=deque([])
        pushed=set()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]==1:
                    queue.append((0,i,j))
                    pushed.add((i,j))
                    isWater[i][j]=0
        while queue:
            h,i,j=queue.popleft()
            DIRS=[(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in DIRS:
                nr,nc=i+dr,j+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in pushed:
                    isWater[nr][nc]=h+1
                    queue.append((h+1,nr,nc))
                    pushed.add((nr,nc))
        return isWater