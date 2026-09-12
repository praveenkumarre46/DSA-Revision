from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        formatted = sorted([[l, r, w, i] for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[0])
        starts = [x[0] for x in formatted]
        
        nxt = [n] * n
        for i in range(n):
            nxt[i] = bisect_left(starts, formatted[i][1] + 1)
        
        memo = {}

        def solve(i, count):
            if count == 0 or i == n:
                return (0, [])
            
            if (i, count) in memo:
                return memo[(i, count)]
            
            skip_w, skip_seq = solve(i + 1, count)
            
            pick_sub_w, pick_sub_seq = solve(nxt[i], count - 1)
            pick_w = formatted[i][2] + pick_sub_w
            pick_seq = sorted([formatted[i][3]] + pick_sub_seq)
            
            if pick_w > skip_w:
                res = (pick_w, pick_seq)
            elif skip_w > pick_w:
                res = (skip_w, skip_seq)
            else:
                if not skip_seq or (pick_seq and pick_seq < skip_seq):
                    res = (pick_w, pick_seq)
                else:
                    res = (skip_w, skip_seq)
                    
            memo[(i, count)] = res
            return res

        return solve(0, 4)[1]