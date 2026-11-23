class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        00   02
          11
        20   22
        """
        
        def backtrack(row, cols, diagnals, cross_diagnals):
            nonlocal res
            if row == n:
                res += 1
                return
            
            for col in range(n):
                if col not in cols and (row + col) not in cross_diagnals and (row - col) not in diagnals:
                    cols.add(col)
                    diagnals.add(row - col)
                    cross_diagnals.add(row + col)

                    backtrack(row + 1, cols, diagnals, cross_diagnals)

                    cols.remove(col)
                    diagnals.remove(row - col)
                    cross_diagnals.remove(row + col)

        res = 0
        backtrack(0, set(), set(), set())
        return res
