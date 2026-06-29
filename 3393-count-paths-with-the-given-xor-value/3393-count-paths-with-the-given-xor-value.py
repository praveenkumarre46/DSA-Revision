class Solution:
    def countPathsWithXorValue(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        MAX_XOR = 16

        dp = [[[0] * MAX_XOR for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                for val in range(MAX_XOR):
                    if dp[i][j][val] == 0:
                        continue

                    if i + 1 < m:
                        nxt = val ^ grid[i + 1][j]
                        dp[i + 1][j][nxt] = (dp[i + 1][j][nxt] + dp[i][j][val]) % MOD

                    if j + 1 < n:
                        nxt = val ^ grid[i][j + 1]
                        dp[i][j + 1][nxt] = (dp[i][j + 1][nxt] + dp[i][j][val]) % MOD

        return dp[m - 1][n - 1][k]