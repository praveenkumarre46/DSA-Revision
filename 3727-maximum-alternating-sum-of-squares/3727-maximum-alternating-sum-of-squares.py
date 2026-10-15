class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x**2 for x in nums])
        n = len(nums)
        
        num_negatives = n // 2
        
        negative_sum = sum(squares[:num_negatives])
        positive_sum = sum(squares[num_negatives:])
        
        return positive_sum - negative_sum