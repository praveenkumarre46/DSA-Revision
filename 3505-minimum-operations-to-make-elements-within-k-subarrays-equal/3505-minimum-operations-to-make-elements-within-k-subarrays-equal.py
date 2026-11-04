from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        costs = [0] * n
        
        sl = SortedList()
        sum_left = 0
        sum_right = 0
        left_count = (x + 1) // 2
        
        for i in range(n):
            val = nums[i]
            sl.add(val)
            idx = sl.bisect_left(val)
            
            if idx < left_count:
                sum_left += val
                if len(sl) > left_count:
                    moved = sl[left_count]
                    sum_left -= moved
                    sum_right += moved
            else:
                sum_right += val
                
            if i >= x:
                out = nums[i - x]
                out_idx = sl.bisect_left(out)
                sl.remove(out)
                if out_idx < left_count:
                    sum_left -= out
                    if len(sl) >= left_count:
                        moved = sl[left_count - 1]
                        sum_right -= moved
                        sum_left += moved
                else:
                    sum_right -= out
                    
            if i >= x - 1:
                median = sl[left_count - 1]
                right_count = x - left_count
                cost = (left_count * median - sum_left) + (sum_right - right_count * median)
                costs[i] = cost

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(x, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]
                if dp[i - x][j - 1] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + costs[i - 1])
                    
        return dp[n][k]