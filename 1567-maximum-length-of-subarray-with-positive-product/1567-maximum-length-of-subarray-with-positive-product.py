class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        first_negative = -1
        zero_pos = -1
        neg_count = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                first_negative = -1
                zero_pos = i
                neg_count = 0
            else:
                if num < 0:
                    neg_count += 1
                    if first_negative == -1:
                        first_negative = i
                
                if neg_count % 2 == 0:
                    max_len = max(max_len, i - zero_pos)
                else:
                    max_len = max(max_len, i - first_negative)
                    
        return max_len