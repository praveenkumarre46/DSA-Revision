import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = [] 
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        
        val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0