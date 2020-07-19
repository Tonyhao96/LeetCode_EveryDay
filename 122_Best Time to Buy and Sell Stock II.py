#122_Best Time to Buy and Sell Stock II

#Find out Valley and Peak
#Time complexity: O(n)  Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, i, n, buy, sell = 0, 0, len(prices) - 1, prices[0], prices[0]
        while i < n:
            while i < n and prices[i+1] < prices[i]:
                i += 1
            buy = prices[i]
            while i < n and prices[i+1] > prices[i]:
                i += 1
            sell = prices[i]
            res += sell - buy
            i += 1
        return res

#Math Optimize(Ignore the buy and sell date)
#Time complexity: O(n)  Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        return res