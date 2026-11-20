class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(curr, left, right):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            
            if left < n:
                curr.append('(')
                backtrack(curr, left + 1, right)
                curr.pop()
            
            if left > right:
                curr.append(')')
                backtrack(curr, left, right + 1)
                curr.pop()
        

        res = []
        backtrack([], 0, 0)
        return res