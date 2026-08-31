class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        - ( - first
        - ) - and then this
        - * - (, ), ""

        ( ( * * )
        ( ( )   )
        ( (   ) )

        * * ( ( )
        * ( * ( )
        """

        # DP - top down
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if (i, open) not in memo:
                if s[i] == '(':
                    memo[(i, open)] = dfs(i + 1, open + 1)
                elif s[i] == ')':
                    memo[(i, open)] = dfs(i + 1, open - 1)
                else:
                    memo[(i, open)] = (dfs(i + 1, open) or
                            dfs(i + 1, open + 1) or
                            dfs(i + 1, open - 1))
            return memo[(i, open)]
        memo = {}
        return dfs(0, 0)

        left = 0
        right = 0
        wildcard = 0
        for ch in s:
            if ch == "(":
                left += 1
            elif ch == ")":
                if left == right and not wildcard:
                    return False
                right += 1
            else:
                wildcard += 1

        return left == right