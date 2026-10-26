class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows=len(grid)
        cols=len(grid[0])
        vis=[[False for _ in range(cols)] for _ in range(rows)]
        prices=[]
        def dfs(row,col):
            vis[row][col]=True
            val=grid[row][col]
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            for r,c in dir:
                nr,nc=row+r,col+c
                if 0<=nr<rows and  0<=nc<cols and not vis[nr][nc] and grid[nr][nc]!=0:
                    val+=dfs(nr,nc)
            return val
        counter=0
        for i in range(rows):
            for j in range(cols):
                if not vis[i][j] and grid[i][j]!=0:
                    vali=dfs(i,j)
                    if vali%k==0:
                        counter+=1
        return counter
            
        