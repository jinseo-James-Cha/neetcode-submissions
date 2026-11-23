class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        00   02
          11
        20   22
        """
        
        def backtrack(row, cols, diagonals, cross_diagonals):
            nonlocal res
            if row == n:
                res += 1
                return
            
            for col in range(n):
                if col not in cols and (row - col) not in diagonals and (row + col) not in cross_diagonals:
                    cols.add(col)
                    diagonals.add(row - col)
                    cross_diagonals.add(row + col)

                    backtrack(row + 1, cols, diagonals, cross_diagonals)

                    cols.remove(col)
                    diagonals.remove(row - col)
                    cross_diagonals.remove(row + col)

        res = 0
        backtrack(0, set(), set(), set())
        return res
