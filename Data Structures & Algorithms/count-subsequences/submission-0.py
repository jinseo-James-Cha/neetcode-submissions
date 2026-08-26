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