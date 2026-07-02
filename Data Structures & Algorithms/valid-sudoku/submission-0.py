class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        rows 9
        cols 9
        sub_boxes 9
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]
        print(sub_boxes)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    current_cell = int(board[row][col])
                    if current_cell in rows[row]:
                        return False
                    elif current_cell in cols[col]:
                        return False
                    elif current_cell in sub_boxes[row // 3][col // 3]:
                        return False
                    
                    rows[row].add(current_cell)
                    cols[col].add(current_cell)
                    sub_boxes[row//3][col//3].add(current_cell)
        
        return True
