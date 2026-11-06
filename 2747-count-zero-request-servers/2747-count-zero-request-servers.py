from collections import defaultdict
from typing import List


class Solution:

    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        logs.sort(key=lambda item: item[1])
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])

        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        active_servers = 0

        left = 0
        right = 0
        num_logs = len(logs)

        for original_idx, q_time in sorted_queries:
            window_start = q_time - x

            while right < num_logs and logs[right][1] <= q_time:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    active_servers += 1
                server_counts[s_id] += 1
                right += 1

            while left < num_logs and logs[left][1] < window_start:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    active_servers -= 1
                left += 1

            ans[original_idx] = n - active_servers

        return ans