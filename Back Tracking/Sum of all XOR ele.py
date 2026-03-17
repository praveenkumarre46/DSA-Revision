class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        OR = 0
        for num in nums:
            OR |= num
        return OR * (1 << (len(nums)-1))
            