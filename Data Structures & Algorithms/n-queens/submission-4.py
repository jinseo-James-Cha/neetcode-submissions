class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        0 0     0 2
            1 1     1 3
        2 0     2 2
            3 1     3 3
        """
        
        def backtrack(board, row, col_set, diag_set, cross_diag_set):
            if row == n:
                copy_board = ["".join(row) for row in board]
                res.append(copy_board)
                return
            
            for col in range(n):
                if col not in col_set and (row-col) not in diag_set and (row+col) not in cross_diag_set:
                    board[row][col] = "Q"
                    col_set.add(col)
                    diag_set.add(row - col)
                    cross_diag_set.add(row + col)
                    
                    backtrack(board, row+1, col_set, diag_set, cross_diag_set)

                    board[row][col] = "."
                    col_set.remove(col)
                    diag_set.remove(row - col)
                    cross_diag_set.remove(row + col)

        board = [["."] * n for _ in range(n)]
        res = []
        backtrack(board, 0, set(), set(), set())
        return res