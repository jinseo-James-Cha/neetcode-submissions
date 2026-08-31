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
        # Greedy
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

        # Stack
        left = []
        wildcard = []
        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                wildcard.append(i)
            else:
                if not left and not wildcard:
                    return False
                
                if left:
                    left.pop()
                else:
                    wildcard.pop()
        while left and wildcard:
            if left.pop() > wildcard.pop():
                return False
        
        return not left

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