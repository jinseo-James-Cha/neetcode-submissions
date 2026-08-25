class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        distinct combination
        """
        # DP - bottom up
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount+1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for remaining in range(1, amount+1):
                total = 0
                if coins[i-1] <= remaining:
                    total += dp[i-1][remaining]
                    total += dp[i][remaining - coins[i-1]]
                else:
                    total += dp[i-1][remaining]
                dp[i][remaining] = total

        return dp[n][amount]
        




        # DP - top down
        def dp(idx, remaining):
            if remaining == 0:
                return 1
            if idx >= len(coins):
                return 0

            if (idx, remaining) not in memo:
                total = 0
                if remaining >= coins[idx]:
                    do_nothing = dp(idx+1, remaining)
                    do_something = dp(idx, remaining - coins[idx])
                    total = do_nothing + do_something
                
                memo[(idx, remaining)] = total

            return memo[(idx, remaining)]
        coins.sort()
        memo = {}
        return dp(0, amount)


        # dfs -> TLE
        def dfs(idx, remaining):
            if remaining == 0:
                return 1

            if idx >= len(coins):
                return 0
            
            res = 0
            if remaining >= coins[idx]:
                res = dfs(idx + 1, remaining)
                res += dfs(idx, remaining - coins[idx])
            return res
        
        coins.sort()
        return dfs(0, amount)

