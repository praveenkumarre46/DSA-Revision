class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols =len(matrix),len(matrix[0])
        memo = {}

        def rec(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            maxl = 1
            for r, c in dire:
                nr, nc = r + i, c + j
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[i][j]:
                    maxl = max(1 + rec(nr, nc), maxl)

            memo[(i, j)] = maxl
            return maxl

        maxl = 0
        for i in range(rows):
            for j in range(cols):
                maxl = max(maxl, rec(i, j))

        return maxl