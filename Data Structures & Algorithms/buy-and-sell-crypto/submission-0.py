class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 0
        max_profit = 0

        while r < len(prices) - 1:
            r += 1
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                l = r

        return max_profit
