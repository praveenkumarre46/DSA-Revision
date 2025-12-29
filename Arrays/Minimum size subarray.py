class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        minlen=float('inf')
        cursum=0
        for right in range(len(nums)):
            cursum+=nums[right]
            if cursum>=target:
                while cursum>=target:
                    minlen=min(minlen,right-left+1)
                    cursum-=nums[left]
                    left+=1
        return minlen if minlen!=float('inf') else 0

        