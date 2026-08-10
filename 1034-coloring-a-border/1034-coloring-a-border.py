class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        orig_color = grid[row][col]
        visited = set()
        borders = set()

        def dfs(r, c):
            visited.add((r, c))
            is_border_cell = False

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != orig_color:
                    is_border_cell = True
                elif (nr, nc) not in visited:
                    dfs(nr, nc)

            if is_border_cell:
                borders.add((r, c))

        dfs(row, col)

        for r, c in borders:
            grid[r][c] = color

        return grid