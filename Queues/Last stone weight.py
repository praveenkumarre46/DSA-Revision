import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        st = [-s for s in stones] 
        heapq.heapify(st)

        while len(st) > 1:
            stone1 = -heapq.heappop(st)
            stone2 = -heapq.heappop(st)
            
            if stone1 != stone2:
                heapq.heappush(st, -(stone1 - stone2))

        return -st[0] if st else 0


        