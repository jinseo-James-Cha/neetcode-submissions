class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP - bottom up
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start_index = 0
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                max_len = 2
                start_index = i
        
        for substring_len in range(3, n + 1):
            for i in range(n - substring_len + 1):
                j = i + substring_len - 1

                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    max_len = substring_len
                    start_index = i
        return s[start_index : start_index + max_len]




        # TWo pointers
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1: right]
        

        longest = ""
        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i+1)
            if len(longest) < len(odd):
                longest = odd
            if len(longest) < len(even):
                longest = even

        return longest