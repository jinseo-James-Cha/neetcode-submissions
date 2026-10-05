class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        # swap left and right
        # n = len(s)
        # if n == 1:
        #     return s
        
        # for i in range(n // 2):
        #     if s[i] != s[n - i - 1]:
        #         s[n - i - 1], s[i] = s[i], s[n - i - 1]
