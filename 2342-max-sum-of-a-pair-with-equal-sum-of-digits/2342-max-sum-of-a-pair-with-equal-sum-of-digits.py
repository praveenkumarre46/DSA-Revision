class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitsum(n):
            sumd = 0
            while n > 0:
                sumd += n % 10
                n //= 10
            return sumd
        dic={}
        maxsum=-1
        for ele in nums:
            ds=digitsum(ele)
            if ds in dic:
                maxsum=max(maxsum,dic[ds]+ele)
                dic[ds]=max(dic[ds],ele)
            else:
                dic[ds]=ele
        return maxsum
