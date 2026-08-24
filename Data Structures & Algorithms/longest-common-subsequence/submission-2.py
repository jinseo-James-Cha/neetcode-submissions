class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
          c a t
        c 1 1 1
        r 1 1 1
        a 1 2 2
        b 1 2 2
        t 1 2 3

          a b c d
        a 1 1 1 1
        b 1 2 2 2
        c 1 2 3
        d
        """
        # DP - bottom up, space optimization
        t1_len = len(text1)
        t2_len = len(text2)
        
        prev_row = [0] * (t2_len + 1)
        for t1_dp_idx in range(1, t1_len + 1):
            curr_row = [0] * (t2_len + 1)

            for t2_dp_idx in range(1, t2_len + 1):
                if text1[t1_dp_idx - 1] == text2[t2_dp_idx - 1]:
                    curr_row[t2_dp_idx] = prev_row[t2_dp_idx - 1] + 1
                else:
                    curr_row[t2_dp_idx] = max(prev_row[t2_dp_idx], curr_row[t2_dp_idx - 1])
            prev_row = curr_row
        return prev_row[t2_len]



        # DP - bottom up
        t1_len = len(text1)
        t2_len = len(text2)
        dp = [[0] * (t2_len + 1) for _ in range(t1_len + 1)]
        for t1_dp_idx in range(1, t1_len + 1):
            for t2_dp_idx in range(1, t2_len + 1):
                if text1[t1_dp_idx-1] == text2[t2_dp_idx-1]:
                    dp[t1_dp_idx][t2_dp_idx] = dp[t1_dp_idx-1][t2_dp_idx-1] + 1
                else:
                    dp[t1_dp_idx][t2_dp_idx] = max(dp[t1_dp_idx][t2_dp_idx-1], dp[t1_dp_idx-1][t2_dp_idx])
        return dp[t1_len][t2_len]


        # DP - top down
        def dp(t1_idx, t2_idx):
            if t1_idx < 0 or t2_idx < 0:
                return 0
            
            if (t1_idx, t2_idx) not in memo:
                curr = 0
                if text1[t1_idx] == text2[t2_idx]:
                    curr = dp(t1_idx - 1, t2_idx - 1) + 1
                else:
                    curr = max(dp(t1_idx-1, t2_idx), dp(t1_idx, t2_idx-1))
                memo[(t1_idx, t2_idx)] = curr
            return memo[(t1_idx, t2_idx)]

        memo = {}
        return dp(len(text1)-1, len(text2)-1)
