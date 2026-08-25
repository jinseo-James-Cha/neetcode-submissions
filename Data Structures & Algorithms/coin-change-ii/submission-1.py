class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        distinct combination
        """
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

