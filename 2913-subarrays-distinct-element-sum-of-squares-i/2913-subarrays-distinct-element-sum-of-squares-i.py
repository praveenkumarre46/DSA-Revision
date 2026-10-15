class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        summ=0
        for i in range(len(nums)):
            sett=set()
            for j in range(i,len(nums)):
                sett.add(nums[j])
                summ+=len(sett)**2
        return summ

        