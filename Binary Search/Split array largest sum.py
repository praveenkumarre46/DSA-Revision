class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            subarray_count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > max_sum:
                    subarray_count += 1
                    current_sum = num
                    if subarray_count > k:
                        return False
                else:
                    current_sum += num
            return True

        low, high = max(nums), sum(nums)
        ans = high
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if can_split(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans