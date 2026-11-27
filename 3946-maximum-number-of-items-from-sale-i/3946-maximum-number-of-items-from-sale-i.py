from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            cost = items[i][1]
            if cost > budget:
                continue
            first_gain = 1 + bonus[i]

            for c in range(budget, cost - 1, -1):
                if dp[c - cost] + first_gain > dp[c]:
                    dp[c] = dp[c - cost] + first_gain

            for c in range(cost, budget + 1):
                if dp[c - cost] + 1 > dp[c]:
                    dp[c] = dp[c - cost] + 1

        return dp[budget]