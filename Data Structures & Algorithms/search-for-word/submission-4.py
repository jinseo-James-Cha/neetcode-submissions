class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS and Backtracking
        if not word:
            return True
        
        if not board or not board[0]:
            return False

        def is_within_bounds(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        DIR = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col, word_idx):
            if word_idx == len(word):
                return True

            temp = board[row][col]
            board[row][col] = '#'

            for dr, dc in DIR:
                next_r, next_c = row + dr, col + dc
                if is_within_bounds(next_r, next_c) and word[word_idx] == board[next_r][next_c]:
                    if dfs(next_r, next_c, word_idx + 1):
                        board[row][col] = temp
                        return True
            
            board[row][col] = temp
            return False
            
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                     if dfs(row, col, 1):
                        return True

        return False