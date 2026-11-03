class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxe=max(nums)
        moves=0
        for ele in nums:
            moves+=maxe-ele
        return moves
        