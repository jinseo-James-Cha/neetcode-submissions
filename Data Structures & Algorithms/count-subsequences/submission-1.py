class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
          c a a a t
        c 1 1 1 1 1
        a 0 1 2 3 3
        t 0 0 0 0 3

          x x y x y - s
        x 1 2 2 3 3
        y 0 0 2 2 5
        |
        t
        """
        # DP - bottom up
        s_len, t_len = len(s), len(t)
        dp = [[0] * (s_len + 1) for _ in range(t_len + 1)]
        for s_idx in range(s_len + 1):
            dp[0][s_idx] = 1
        
        for t_idx in range(1, t_len + 1):
            for s_idx in range(1, s_len + 1):
                if t[t_idx-1] == s[s_idx-1]:
                    dp[t_idx][s_idx] = dp[t_idx - 1][s_idx - 1] + dp[t_idx][s_idx-1]
                else:
                    dp[t_idx][s_idx] = dp[t_idx][s_idx - 1]
        return dp[t_len][s_len]



        # DP - top down
        def dp(s_idx, t_idx):
            if t_idx < 0:
                return 1

            if s_idx < 0:
                return 0
            
            if (s_idx, t_idx) not in memo:
                total = 0
                if s[s_idx] == t[t_idx]:
                    total = dp(s_idx - 1, t_idx) + dp(s_idx-1, t_idx-1)
                else:
                    total = dp(s_idx - 1, t_idx)
                
                memo[(s_idx, t_idx)] = total
            return memo[(s_idx, t_idx)]

        memo = {}
        return dp(len(s) - 1, len(t) - 1)