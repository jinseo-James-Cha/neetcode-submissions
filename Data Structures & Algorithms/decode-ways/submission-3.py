class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i):
            if i == len(s):
                return 1
            
            if i not in memo:
                total = 0
                if 1 <= int(s[i]) <= 9:
                    total += dp(i+1)
                
                if 10 <= int(s[i:i+2]) <= 26:
                    total += dp(i+2)
                memo[i] = total
            
            return memo[i]
            
        memo = {}
        return dp(0)
