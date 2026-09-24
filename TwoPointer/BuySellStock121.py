class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(len(prices)):
            if prices[l] < prices [r]:

                price = prices[r] - prices [l]
                profit = max(profit, price)
            else:
                l = r
            r += 1
        return profit