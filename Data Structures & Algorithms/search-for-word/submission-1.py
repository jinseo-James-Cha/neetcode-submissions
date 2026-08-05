class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def is_within_bounds(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        DIRS = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(row, col, visited, word_idx):
            if word_idx == len(word) - 1:
                return True
            
            for dy, dx in DIRS:
                next_r, next_c = row+dy, col+dx
                if is_within_bounds(next_r, next_c) and (next_r, next_c) not in visited and word[word_idx+1] == board[next_r][next_c]:
                    
                    visited.add((next_r, next_c))
                    if dfs(next_r, next_c, visited, word_idx + 1):
                        return True
                    visited.remove((next_r, next_c))
            
            return False
        
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r,c, {(r, c)}, 0):
                        return True
        return False