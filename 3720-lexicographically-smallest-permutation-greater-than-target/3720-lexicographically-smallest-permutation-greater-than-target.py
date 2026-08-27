from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        n = len(s)
        
        for i in range(n, -1, -1):
            prefix_counts = Counter(target[:i])
            if any(prefix_counts[ch] > counts[ch] for ch in prefix_counts):
                continue
            
            rem_counts = counts - prefix_counts
            
            if i == n:
                continue
            
            target_char = target[i]
            for ch in sorted(rem_counts.keys()):
                if ch > target_char and rem_counts[ch] > 0:
                    rem_counts[ch] -= 1
                    tail = "".join(c * rem_counts[c] for c in sorted(rem_counts.keys()))
                    return target[:i] + ch + tail
                    
        return ""