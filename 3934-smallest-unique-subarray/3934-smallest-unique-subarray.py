from typing import List
from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9
        BASE1, BASE2 = 1315423911, 2654435761
        
        def has_unique_subarray(length: int) -> bool:
            if length == n:
                return True
            
            p1 = pow(BASE1, length - 1, MOD1)
            p2 = pow(BASE2, length - 1, MOD2)
            
            h1 = h2 = 0
            for i in range(length):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2
            
            counts = Counter([(h1, h2)])
            
            for i in range(length, n):
                out_val = nums[i - length]
                in_val = nums[i]
                
                h1 = ((h1 - out_val * p1) * BASE1 + in_val) % MOD1
                h2 = ((h2 - out_val * p2) * BASE2 + in_val) % MOD2
                
                counts[(h1, h2)] += 1
            
            return any(freq == 1 for freq in counts.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_subarray(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans