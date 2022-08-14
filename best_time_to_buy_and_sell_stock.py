class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = 10000000000
        profit = 0
        
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            profit = max(profit,prices[i]-mini)
                
        return profit
