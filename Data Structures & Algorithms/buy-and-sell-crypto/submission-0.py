class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            bp = prices[i]
            for j in range(i+1, len(prices)):
                sp = prices[j]
                profit = sp - bp
                if profit > max_profit:
                    max_profit = profit
        return max_profit  