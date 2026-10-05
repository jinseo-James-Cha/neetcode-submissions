class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        for i in range(max(m, n)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res)
        
        
        w1_idx = w2_idx = 0
        w1_len = len(word1)
        w2_len = len(word2)
        
        res = []
        while w1_idx < w1_len and w2_idx < w2_len:
            res.append(word1[w1_idx])
            res.append(word2[w2_idx])

            w1_idx += 1
            w2_idx += 1
        
        res.extend(word1[w1_idx:])
        res.extend(word2[w2_idx:])
        return "".join(res)