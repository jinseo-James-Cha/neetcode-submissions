class Solution:
    def numDecodings(self, s: str) -> int:
        # DP - bottom up, space optimized
        two_back = 1
        one_back = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):
            curr = one_back if s[i-1] != "0" else 0
            curr += two_back if 10 <= int(s[i-2:i]) <= 26 else 0
            
            two_back = one_back
            one_back = curr
        return one_back


        # DP - bottom up
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]


        # DP - top down
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
