class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        premax=[nums[0]]
        for ele in nums[1:]:
            if ele >= premax[-1]:
                premax.append(ele)
            else:
                premax.append(premax[-1])
        postmin=[0]*len(nums)
        postmin[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=postmin[i+1]:
                postmin[i]=nums[i]
            else:
                postmin[i]=postmin[i+1]
        ind=float('inf')
        for i in range(len(nums)):
            if premax[i]-postmin[i]<=k:
                ind=min(ind,i)
        return ind if ind!=float('inf') else -1
            
        