class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self._build(arr, node * 2 + 1, start, mid)
        self._build(arr, node * 2 + 2, mid + 1, end)
        self.tree[node] = self.tree[node * 2 + 1] ^ self.tree[node * 2 + 2]

    def update(self, idx, val, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(idx, val, node * 2 + 1, start, mid)
        else:
            self.update(idx, val, node * 2 + 2, mid + 1, end)
        self.tree[node] = self.tree[node * 2 + 1] ^ self.tree[node * 2 + 2]

    def query(self, l, r, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(l, r, node * 2 + 1, start, mid)
        p2 = self.query(l, r, node * 2 + 2, mid + 1, end)
        return p1 ^ p2


class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        self.cur_pos = 0

        def dfs(u, p):
            size = 1
            max_c_size = 0
            for v in adj[u]:
                if v != p:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    c_size = dfs(v, u)
                    size += c_size
                    if c_size > max_c_size:
                        max_c_size = c_size
                        heavy[u] = v
            return size

        def decompose(u, h):
            head[u] = h
            pos[u] = self.cur_pos
            self.cur_pos += 1
            if heavy[u] != -1:
                decompose(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    decompose(v, v)

        dfs(0, -1)
        decompose(0, 0)

        arr = [0] * n
        for i in range(n):
            arr[pos[i]] = 1 << (ord(s[i]) - ord("a"))

        seg_tree = SegmentTree(arr)

        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res ^= seg_tree.query(pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= seg_tree.query(pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                mask = 1 << (ord(c) - ord("a"))
                seg_tree.update(pos[u], mask)
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans