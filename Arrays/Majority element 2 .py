class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        cand1, count1 = None, 0
        cand2, count2 = None, 0

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        limit = len(nums) // 3
        
        for cand in [cand1, cand2]:
            if cand is not None:
                actual_count = 0
                for n in nums:
                    if n == cand:
                        actual_count += 1
                if actual_count > limit:
                    result.append(cand)

        return result