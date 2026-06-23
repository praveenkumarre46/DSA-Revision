class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for i in range(len(intervals)):
            starts.append([intervals[i][0], i])
        starts.sort(key=lambda x: x[0])
        
        res = []
        n = len(intervals)
        
        for interval in intervals:
            target = interval[1]
            left, right = 0, n - 1
            ans_idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                if starts[mid][0] >= target:
                    ans_idx = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
                    
            res.append(ans_idx)
            
        return res