class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # n e e t  n = 4
        # 0 1 2 3

        n = len(s)
        if n == 1:
            return s
        
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                s[n - i - 1], s[i] = s[i], s[n - i - 1]
        return s