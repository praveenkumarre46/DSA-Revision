class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum_d = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (l + r) // 2
            self._apply(2 * node, l, mid, val)
            self._apply(2 * node + 1, mid + 1, r, val)
            self.lazy[node] = 0

    def _apply(self, node, l, r, val):
        length = r - l + 1
        MOD = 10**9 + 7
        self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum_d[node] + val * val * length) % MOD
        self.sum_d[node] = (self.sum_d[node] + val * length) % MOD
        self.lazy[node] = (self.lazy[node] + val) % MOD

    def update(self, node, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self._apply(node, l, r, val)
            return

        self._push(node, l, r)
        mid = (l + r) // 2
        
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)

        MOD = 10**9 + 7
        self.sum_d[node] = (self.sum_d[2 * node] + self.sum_d[2 * node + 1]) % MOD
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % MOD

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = SegmentTree(n)
        last_occurrence = {}
        ans = 0

        for j, val in enumerate(nums):
            prev_idx = last_occurrence.get(val, -1)
            tree.update(1, 0, n - 1, prev_idx + 1, j, 1)
            ans = (ans + tree.sum_sq[1]) % MOD
            last_occurrence[val] = j

        return ans