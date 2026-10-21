class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = sorted(s)
        target = "".join(t)
        
        if s == target:
            return 0
        
        if n < 2 or (n == 2 and s[0] > s[1]):
            return -1
        
        if s[0] == target[0] or s[-1] == target[-1]:
            return 1
            
        if s[0] == target[-1] and s[-1] == target[0]:
            if min(s[:n-1]) == target[0] or max(s[1:]) == target[-1]:
                return 2
            return 3
            
        return 2