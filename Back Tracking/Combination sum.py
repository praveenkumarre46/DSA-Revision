class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subs=[]
        def rec(i,cur,cursum):
            if cursum==target:
                subs.append(cur.copy())
                return 
            if cursum > target or i==len(nums):
                return 
            cur.append(nums[i])
            rec(i, cur, cursum + nums[i])
            cur.pop()
            rec(i+1, cur, cursum)
        rec(0,[],0)
        return subs
        