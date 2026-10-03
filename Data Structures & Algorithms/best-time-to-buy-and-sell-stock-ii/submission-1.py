class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP - bottom up
        dp = [[0] * 2 for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            dp[i][0] = max(dp[i+1][0], -prices[i] + dp[i+1][1])
            dp[i][1] = max(dp[i+1][1], prices[i] + dp[i+1][0])
        
        return dp[0][0]

        # DP - top down
        def dp(i, is_hold):
            if i == len(prices):
                return 0
            
            if (i, is_hold) not in memo:
                do_nothing = dp(i + 1, is_hold)
                do_something = 0
                if is_hold:
                    do_something = dp(i+1, False) + prices[i]
                else:
                    do_something = dp(i+1, True) - prices[i]
                
                memo[(i, is_hold)] = max(do_nothing, do_something)
            return memo[(i, is_hold)]
        
        memo = {}
        return dp(0, False)