class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp - bottom up
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for remaining in range(1, amount + 1):
            for coin in coins:
                if remaining >= coin:
                    dp[remaining] = min(dp[remaining], 1 + dp[remaining - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
        
        # dp - top down
        def dp(remaining):
            if remaining == 0:
                return 0
            
            if remaining not in memo:
                res = float('inf')
                for coin in coins:
                    if remaining >= coin:
                        res = min(res, 1 + dp(remaining - coin))
                memo[remaining] = res

            return memo[remaining]

        memo = {}
        min_coins = dp(amount)
        return min_coins if min_coins != float('inf') else -1



        # Backtrack -> O(3^n) -> TLE
        def backtrack(curr, remaining):
            nonlocal minimum_coins
            if remaining == 0:
                minimum_coins = min(len(curr), minimum_coins)
                return
            
            for coin in coins:
                if coin <= remaining:
                    curr.append(coin)
                    backtrack(curr, remaining - coin)
                    curr.pop()

        coins.sort(reverse=True)
        minimum_coins = float('inf')
        backtrack([], amount)
        return minimum_coins if minimum_coins != float('inf') else -1