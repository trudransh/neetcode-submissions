class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxP = 0

        for i in prices:
            if maxP < i - minbuy:
                maxP = i - minbuy
            if i < minbuy:
                minbuy = i
        return maxP