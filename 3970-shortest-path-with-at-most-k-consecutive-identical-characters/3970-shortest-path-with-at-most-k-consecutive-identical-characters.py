import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        dist = {}
        dist[(0, 1)] = 0
        
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if d > dist.get((u, count), float('inf')):
                continue
                
            if u == n - 1:
                return d
                
            for v, w in adj[u]:
                next_count = count + 1 if labels[u] == labels[v] else 1
                if next_count <= k:
                    if d + w < dist.get((v, next_count), float('inf')):
                        dist[(v, next_count)] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))
                        
        return -1