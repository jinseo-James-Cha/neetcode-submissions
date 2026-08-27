class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        3 operations
        insert
        delete
        replace

        return minimum number of operations
        making from word1 to word2

            m o n k e y s
            m o n   e y
            0 1 2 3 4 5 6
        """
        # DP - bottom up
        dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
        return dp[0][0]





        # DP - top down
        if word1 == word2:
            return 0
        
        def dp(w1_idx, w2_idx):
            if w1_idx >= len(word1):
                return len(word2) - w2_idx
            
            if w2_idx >= len(word2):
                return len(word1) - w1_idx

            if (w1_idx, w2_idx) not in memo:
                if word1[w1_idx] == word2[w2_idx]:
                    memo[(w1_idx, w2_idx)] = dp(w1_idx + 1, w2_idx + 1)
                else:
                    insert = dp(w1_idx, w2_idx + 1)
                    delete = dp(w1_idx + 1, w2_idx)
                    replace = dp(w1_idx + 1, w2_idx + 1)

                    memo[(w1_idx, w2_idx)] = min(insert, delete, replace) + 1
            return memo[(w1_idx, w2_idx)]

        memo = {}
        return dp(0, 0)




