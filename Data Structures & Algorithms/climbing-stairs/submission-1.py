class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 step or 2steps at a time
        reach n stairs        

        1

        1 1
        2

        1 1 1
        1 2
        2 1

        1 1 1 1
        1 2 1
        1 1 2
        2 1 1
        2 2
        """
        # DP - bottom up
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # DP - top down
        def dp(n):
            if n <= 2:
                return n

            if n not in memo:
                memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        
        memo = {}
        return dp(n)