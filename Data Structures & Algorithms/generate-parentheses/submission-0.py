class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        ( need to have more than )

            (
        ((       ()
    (((     (()
        """

        def backtrack(curr, number_of_open, number_of_close):
            if number_of_open + number_of_close == n * 2:
                res.append("".join(curr))
                return
            
            if number_of_open < n:
                curr.append('(')
                backtrack(curr, number_of_open + 1, number_of_close)
                curr.pop()
            
            if number_of_close < number_of_open:
                curr.append(')')
                backtrack(curr, number_of_open, number_of_close + 1)
                curr.pop()

        res = []
        backtrack([], 0, 0)
        return res