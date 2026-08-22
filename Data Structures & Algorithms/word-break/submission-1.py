class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
