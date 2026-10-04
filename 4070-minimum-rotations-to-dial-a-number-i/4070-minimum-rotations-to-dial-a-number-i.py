class Solution:
    def minRotations(self, s: str) -> int:
        count = 0
        prev = 0
        for c in s:
            curr = int(c)
            diff = abs(prev - curr)
            count += min(diff, 10 - diff)
            prev = curr
        return count