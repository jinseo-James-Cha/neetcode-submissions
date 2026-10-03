class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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