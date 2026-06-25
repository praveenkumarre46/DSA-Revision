from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        target_mask = (1 << n) - 1
        
        dp = [[-1] * n for _ in range(1 << n)]
        
        def solve(mask: int, last_idx: int) -> int:
            if mask == target_mask:
                return 1
            
            if dp[mask][last_idx] != -1:
                return dp[mask][last_idx]
            
            count = 0
            for i in range(n):
                if not (mask & (1 << i)):
                    if nums[last_idx] % nums[i] == 0 or nums[i] % nums[last_idx] == 0:
                        count = (count + solve(mask | (1 << i), i)) % MOD
                        
            dp[mask][last_idx] = count
            return count

        total_permutations = 0
        for i in range(n):
            total_permutations = (total_permutations + solve(1 << i, i)) % MOD
            
        return total_permutations