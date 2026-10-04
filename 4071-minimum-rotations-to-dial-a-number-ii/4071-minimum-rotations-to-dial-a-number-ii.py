class Solution:
    def minRotations(self, n: int, s: str) -> int:
        velmotrani = s
        
        digits = [int(c) for c in s]
        
        def dist(a, b):
            d = abs(a - b)
            return min(d, 10 - d)

        pref = [0] * (n + 1)
        prev = 0
        for i in range(n):
            pref[i + 1] = pref[i] + dist(prev, digits[i])
            prev = digits[i]

        suf_rev = [0] * (n + 1)
        for i in range(n - 2, -1, -1):
            suf_rev[i] = suf_rev[i + 1] + dist(digits[i + 1], digits[i])

        ans = pref[n]

        for k in range(n):
            cost_prefix = pref[k]
            last_prefix_digit = 0 if k == 0 else digits[k - 1]
            cost_transition = dist(last_prefix_digit, digits[n - 1])
            cost_suffix = suf_rev[k]
            
            total_cost = cost_prefix + cost_transition + cost_suffix
            if total_cost < ans:
                ans = total_cost

        return ans