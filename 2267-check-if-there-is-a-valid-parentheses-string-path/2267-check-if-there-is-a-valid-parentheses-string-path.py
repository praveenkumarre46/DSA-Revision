class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        memo = {}

        def dfs(r, c, balance):
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0 or balance > (m + n - 1) // 2:
                return False

            if r == m - 1 and c == n - 1:
                return balance == 0

            state = (r, c, balance)
            if state in memo:
                return memo[state]

            res = False
            if r + 1 < m and dfs(r + 1, c, balance):
                res = True
            elif c + 1 < n and dfs(r, c + 1, balance):
                res = True

            memo[state] = res
            return res

        return dfs(0, 0, 0)