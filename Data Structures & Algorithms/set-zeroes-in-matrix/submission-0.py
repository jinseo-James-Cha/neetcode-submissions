class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        """
        1 2 3 -> 1 0 3
        4 0 5 -> 0 0 0
        6 7 8 -> 6 0 8

        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        rowZero = True
                    else:
                        matrix[r][0] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0