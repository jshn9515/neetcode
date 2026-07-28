class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_profit = 0
        while r < len(prices) - 1:
            r += 1
            if prices[r] - prices[l] > 0:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r

        return max_profit
