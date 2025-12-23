class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final = []
        for j in range(len(nums)-3):
            if j>0 and nums[j]==nums[j-1]:
                continue
            for i in range(j+1,len(nums) - 2):
                if i > j+1 and nums[i] == nums[i-1]:
                    continue
                    
                left = i + 1
                right = len(nums) - 1
                
                while left < right:
                    total = nums[j]+ nums[i] + nums[left] + nums[right]
                    
                    if total == target:
                        final.append([nums[j],nums[i], nums[left], nums[right]])
                        
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
            
        return final
        