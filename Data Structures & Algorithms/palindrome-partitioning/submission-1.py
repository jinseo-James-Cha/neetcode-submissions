class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(substring):
            left = 0
            right = len(substring) - 1
            while left < right:
                if substring[left] != substring[right]:
                    return False
                
                left += 1
                right -= 1
            return True
        


        def dfs(curr, start):
            if start == len(s):
                res.append(curr[:])
                return

            for i in range(start, len(s)):
                if is_palindrome(s[start:i + 1]):
                    curr.append(s[start:i + 1])
                    dfs(curr, i + 1)
                    curr.pop()
        res = []
        dfs([], 0)
        return res