import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt != 0:
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time