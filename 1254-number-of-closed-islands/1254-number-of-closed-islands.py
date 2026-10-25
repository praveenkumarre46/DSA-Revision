class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            
            visited.add((r, c))
            
            is_closed = True
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                is_closed = False

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    if not dfs(nr, nc):
                        is_closed = False

            return is_closed

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if dfs(i, j):
                        count += 1

        return count