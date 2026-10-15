class Solution:
    def isValid(self, s: str) -> bool:
        """
        open and then close with same type

        """

        # stack
        stack = []
        pairs = {'{' : '}', '[': ']', '(': ')'}

        for p in s:
            if p in pairs: # open
                stack.append(p)
            else: # close
                if not stack: # empty open
                    return False
                
                if pairs[stack[-1]] != p:
                    return False
                
                stack.pop()
        
        return not stack
