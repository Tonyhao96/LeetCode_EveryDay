# 121_Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, float('inf')
        for i in prices:
            buy, profit = min(buy, i), max(profit, i-buy)
        return profit
