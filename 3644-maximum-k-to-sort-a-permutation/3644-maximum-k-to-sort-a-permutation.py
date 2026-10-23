from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a: int, b: int) -> None:
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pa] = pb

from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1 
        
        for i, val in enumerate(nums):
            if i != val:
                if res == -1:
                    res = val
                else:
                    res &= val
        
        return res if res != -1 else 0