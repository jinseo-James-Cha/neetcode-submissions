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
        def dfs(row, col, word_idx, visited):
            if word_idx == len(word):
                return True
            
            for dr, dc in DIR:
                next_r, next_c = row + dr, col + dc
                if is_within_bounds(next_r, next_c) and (next_r, next_c) not in visited and word[word_idx] == board[next_r][next_c]:
                    visited.add((next_r, next_c))
                    if dfs(next_r, next_c, word_idx + 1, visited):
                        return True
                    visited.remove((next_r, next_c))
            
            return False
            
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                     if dfs(row, col, 1, {(row, col)}):
                        return True

        return False