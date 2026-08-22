class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP - Bottom up
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            if not dp[i]:
                continue

            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i + len(w)] = True
        
        return dp[len(s)]



        # DP - top down + hashset
        def dp(i):
            if i in memo:
                return memo[i]

            memo[i] = False
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in words_set:
                    if dp(j):
                        memo[i] = True
                        break

            return memo[i]

        memo = {len(s): True}
        words_set = set(wordDict)
        return dp(0)
        
        # DP - top down
        def dp(i):
            if i in memo:
                return memo[i]

            memo[i] = False
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dp(i + len(w)):
                        memo[i] = True
                        break
            return memo[i]
        memo = {len(s): True}
        return dp(0)
        
        # DFS -> TLE
        def dfs(idx):
            if idx == len(s):
                return True
            
            for word in wordDict:
                if idx + len(word) <= len(s) and s[idx: idx+len(word)] == word:
                    if dfs(idx + len(word)):
                        return True
            return False
        return dfs(0)
