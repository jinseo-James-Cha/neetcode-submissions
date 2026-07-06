class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        make maximum profit.
        choose buy day and sell day
        """


        # brute force
        maximum_profit = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1, n):
                if prices[j] > prices[i]:
                    maximum_profit = max(maximum_profit, prices[j] - prices[i])
        return maximum_profit
        