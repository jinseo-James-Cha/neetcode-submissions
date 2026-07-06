class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        make maximum profit.
        choose buy day and sell day
        """
        # DP
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit






        # brute force
        # O(n^2)
        maximum_profit = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1, n):
                if prices[j] > prices[i]:
                    maximum_profit = max(maximum_profit, prices[j] - prices[i])
        return maximum_profit
        