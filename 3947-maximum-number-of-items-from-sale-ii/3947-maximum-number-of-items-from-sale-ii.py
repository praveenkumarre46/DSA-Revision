from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        for f, _ in items:
            freq[f] += 1
        
        div_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for multiple in range(f, n + 1, f):
                    div_count[f] += freq[multiple]
                div_count[f] -= 1
        
        sorted_items = sorted(items, key=lambda x: x[1])
        min_price = sorted_items[0][1]
        
        ans = 0
        rem_budget = budget
        
        for f, p in sorted_items:
            gain = div_count[f]
            if gain == 0:
                continue
            
            if p >= 2 * min_price:
                break
            
            can_buy = min(gain, rem_budget // p)
            ans += can_buy * 2
            rem_budget -= can_buy * p
            
            if can_buy < gain:
                break
                
        ans += rem_budget // min_price
        return ans