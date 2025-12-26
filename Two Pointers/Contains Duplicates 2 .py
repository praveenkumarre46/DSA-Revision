class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for ind,val in enumerate(nums):
            if val in dic:
                if abs(ind-dic[val])<=k:
                    return True
            dic[val]=ind
        return False

        