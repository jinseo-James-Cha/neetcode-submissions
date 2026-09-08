class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        """
        1 2 3 -> 1 0 3
        4 0 5 -> 0 0 0
        6 7 8 -> 6 0 8

        """
        m, n = len(matrix), len(matrix[0])

        # check first row has zero
        first_row_has_zero = False
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break
        
        # check first col has zero
        first_col_has_zero = False
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        # mark first row or col if there is 0 in it
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # update other row and col if there is marker
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # if first row has zero already without marker, update too
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0

        # col too
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0