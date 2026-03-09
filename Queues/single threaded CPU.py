import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()
        
        res = []
        min_heap = []
        i = 0
        time = tasks[0][0]
        
        while i < len(tasks) or min_heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not min_heap:
                time = tasks[i][0]
                continue
            
            proc_time, index = heapq.heappop(min_heap)
            time += proc_time
            res.append(index)
            
        return res