class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
   
        curmin = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < curmin:
                curmin = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - curmin)
                
        return max_profit