class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            
            required_days = 1
            current = 0
            
            for w in weights:
                if current + w > mid:
                    required_days += 1
                    current = 0
                current += w
            
            if required_days <= days:
                right = mid
            else:
                left = mid + 1

        return left

            