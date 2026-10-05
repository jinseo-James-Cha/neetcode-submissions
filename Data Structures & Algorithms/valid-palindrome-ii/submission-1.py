class Solution:
    def validPalindrome(self, s: str) -> bool:
        def dp(left, right, wildcard):
            if left >= right:
                return True

            if (left,right, wildcard) not in memo:
                if s[left] != s[right]:
                    if wildcard:
                        memo[(left,right, wildcard)] = dp(left+1, right, False) or dp(left, right -1, False)
                    else:
                        memo[(left,right, wildcard)] = False
                else:
                    memo[(left,right, wildcard)] = dp(left + 1, right - 1, wildcard)
            return memo[(left,right, wildcard)]
                
        memo = {}
        return dp(0, len(s) - 1, True)