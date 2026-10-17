class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        arr = [(get_digit_sum(val), val, i) for i, val in enumerate(nums)]
        arr.sort()

        visited = [False] * n
        min_swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1

            if cycle_size > 1:
                min_swaps += cycle_size - 1

        return min_swaps