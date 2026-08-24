class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        sell -> cannot buy one on the next day
        own at most one

        buy -> sell -> cooldown -> buy...
        """

        # DP - top down
        def dp(idx, is_holding):
            if idx >= len(prices):
                return 0
            
            if (idx, is_holding) not in memo:
                do_something = 0
                if is_holding:
                    do_something = prices[idx] + dp(idx + 2, False)
                else:
                    do_something = -prices[idx]+dp(idx+1, True)
                
                do_nothing = dp(idx+1, is_holding)

                memo[(idx, is_holding)] = max(do_something, do_nothing)
            return memo[(idx, is_holding)]
                


        
        memo = {}
        return dp(0, False)