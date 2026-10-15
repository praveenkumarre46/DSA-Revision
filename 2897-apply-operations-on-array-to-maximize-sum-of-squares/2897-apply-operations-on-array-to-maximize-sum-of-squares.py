class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 31
        
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bit_count[i] += 1
                    
        ans = 0
        for _ in range(k):
            val = 0
            for i in range(31):
                if bit_count[i] > 0:
                    val |= (1 << i)
                    bit_count[i] -= 1
            ans = (ans + val * val) % MOD
            
        return ans