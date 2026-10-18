class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            return (math.comb(len(left) + len(right), len(left)) * ways(left) * ways(right)) % MOD

        import math
        return (ways(nums) - 1) % MOD