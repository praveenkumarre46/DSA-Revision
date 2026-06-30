class Solution:
    def makeParityAlternating(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return [0, 0]
        
        cost0 = 0
        cost1 = 0
        
        for i, x in enumerate(nums):
            actual_parity = abs(x) % 2
            expected_parity_p0 = i % 2
            
            if actual_parity != expected_parity_p0:
                cost0 += 1
            else:
                cost1 += 1
                
        min_ops = min(cost0, cost1)
        min_range = float('inf')
        
        patterns_to_check = []
        if cost0 == min_ops:
            patterns_to_check.append(0)
        if cost1 == min_ops:
            patterns_to_check.append(1)
            
        for pattern in patterns_to_check:
            candidates = []
            for i, x in enumerate(nums):
                actual_parity = abs(x) % 2
                expected_parity = (i % 2) if pattern == 0 else (1 - (i % 2))
                
                if actual_parity == expected_parity:
                    candidates.append([x])
                else:
                    candidates.append([x - 1, x + 1])
            
            all_options = []
            for idx, opts in enumerate(candidates):
                for val in opts:
                    all_options.append((val, idx))
            
            all_options.sort()
            
            from collections import defaultdict
            counts = defaultdict(int)
            left = 0
            distinct_indices = 0
            
            for right in range(len(all_options)):
                val_r, idx_r = all_options[right]
                if counts[idx_r] == 0:
                    distinct_indices += 1
                counts[idx_r] += 1
                
                while distinct_indices == n:
                    val_l, idx_l = all_options[left]
                    current_range = val_r - val_l
                    if current_range < min_range:
                        min_range = current_range
                        
                    counts[idx_l] -= 1
                    if counts[idx_l] == 0:
                        distinct_indices -= 1
                    left += 1
                    
        return [min_ops, min_range]