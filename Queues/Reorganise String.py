import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(max_heap)
        
        res = []
        prev_count, prev_char = 0, ""
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
            
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_count, prev_char = count + 1, char
            
        result_str = "".join(res)
        return result_str if len(result_str) == len(s) else ""