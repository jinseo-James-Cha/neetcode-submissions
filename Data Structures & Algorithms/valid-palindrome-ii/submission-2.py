class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (
                    is_palindrome(left + 1, right)
                    or is_palindrome(left, right - 1)
                )
            left += 1
            right -= 1

        return True


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