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




