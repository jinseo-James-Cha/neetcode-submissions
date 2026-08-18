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
        # DP - bottom up space optimized
        if n <= 2:
            return n
        two_prev = 1
        one_prev = 2
        for i in range(3, n+1):
            curr = two_prev + one_prev
            two_prev = one_prev
            one_prev = curr
        return one_prev

        # DP - bottom up
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
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