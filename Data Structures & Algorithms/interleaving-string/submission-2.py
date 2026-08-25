class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP - bottom up
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]
        
        # DP - top down
        def dp(s1_idx, s2_idx):
            if s1_idx + s2_idx == len(s3):
                if s1_idx == len(s1) and s2_idx == len(s2):
                    return True
                return False
            
            if (s1_idx, s2_idx) not in memo:
                res = False
                if s1_idx < len(s1) and s1[s1_idx] == s3[s1_idx + s2_idx]:
                    res = dp(s1_idx + 1, s2_idx)
                
                if s2_idx < len(s2) and s2[s2_idx] == s3[s1_idx + s2_idx]:
                    res = res or dp(s1_idx, s2_idx + 1)
                memo[(s1_idx, s2_idx)] = res
            return memo[(s1_idx, s2_idx)]

        memo = {}
        return dp(0, 0)