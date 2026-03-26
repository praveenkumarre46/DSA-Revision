from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def rec(start, path):
            res.append(path.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                rec(i + 1, path)
                path.pop()

        rec(0, [])
        return res