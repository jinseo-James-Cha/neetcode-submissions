class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP - top down
        def dp(s1_idx, s2_idx):
            if s1_idx + s2_idx == len(s3):
                if s1_idx == len(s1) and s2_idx == len(s2):
                    return True
                return False
            
            if (s1_idx, s2_idx) not in memo:
                # using s1
                res = False
                if s1_idx < len(s1) and s1[s1_idx] == s3[s1_idx + s2_idx]:
                    res = dp(s1_idx + 1, s2_idx)
                
                if s2_idx < len(s2) and s2[s2_idx] == s3[s1_idx + s2_idx]:
                    res = res or dp(s1_idx, s2_idx + 1)
                memo[(s1_idx, s2_idx)] = res
            return memo[(s1_idx, s2_idx)]

        memo = {}
        return dp(0, 0)