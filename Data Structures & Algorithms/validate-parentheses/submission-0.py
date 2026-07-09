class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}

        for p in s:
            if p not in pairs:
                stack.append(p)
            elif stack and  pairs[p] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False