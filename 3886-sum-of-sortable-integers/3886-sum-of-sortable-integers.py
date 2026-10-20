
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)

        def is_rotation(block, target):
            k = len(block)
            doubled = block + block

            # Build the KMP LPS array for target
            lps = [0] * k
            j = 0

            for i in range(1, k):
                while j > 0 and target[i] != target[j]:
                    j = lps[j - 1]

                if target[i] == target[j]:
                    j += 1

                lps[i] = j

            # Search target in doubled, allowing starts
            # only in the first k positions
            j = 0

            for i in range(2 * k - 1):
                while j > 0 and doubled[i] != target[j]:
                    j = lps[j - 1]

                if doubled[i] == target[j]:
                    j += 1

                if j == k:
                    return True

            return False

        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target = s[start:start + k]

                if not is_rotation(block, target):
                    valid = False
                    break

            if valid:
                ans += k

        return ans
