class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        premax=[nums[0]]
        for i in range(1,len(nums)):
            if premax[-1]<nums[i]:
                premax.append(nums[i])
            else:
                premax.append(premax[-1])
        postmin=[float("inf")]*len(nums)
        postmin[-1]=nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postmin[i] = min(nums[i], postmin[i + 1])
        for i in range(len(nums)):
            inscore=premax[i]-postmin[i]
            if inscore<=k:
                return i
        return -1