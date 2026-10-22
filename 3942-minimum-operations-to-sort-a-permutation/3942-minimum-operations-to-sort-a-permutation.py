class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        inc_count = 0
        dec_count = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                inc_count += 1
            if nums[i] < nums[(i + 1) % n]:
                dec_count += 1
        
        is_cyclically_inc = (inc_count <= 1)
        is_cyclically_dec = (dec_count <= 1)
        
        if not is_cyclically_inc and not is_cyclically_dec:
            return -1
        
        idx_zero = nums.index(0)
        
        if is_cyclically_inc:
            ans = idx_zero
            rev_then_rot_then_rev = (n - idx_zero) % n + 2
            ans = min(ans, rev_then_rot_then_rev)
            return ans
        else:
            rot_then_rev = (idx_zero + 1) % n + 1
            rev_then_rot = (n - 1 - idx_zero) % n + 1
            return min(rot_then_rev, rev_then_rot)