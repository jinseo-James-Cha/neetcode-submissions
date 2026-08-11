from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        'X':
        'O':

        connect: horizontally or vertically
        region: connect every 'O' cell. any shape
        surround: on the edge of the board
        """
        # BFS
        m, n = len(board), len(board[0])
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def is_within_bounds(row, col):
            return 0 <= row < m and 0 <= col < n
        
        queue = deque()
        for row in range(m):
            for col in range(n):
                if (row == 0 or row == m-1 or col == 0 or col == n-1) and board[row][col] == "O":
                    queue.append((row, col))
        
        while queue:
            curr_r, curr_c = queue.popleft()
            board[curr_r][curr_c] = "T"
            for dy, dx in DIRS:
                next_r, next_c = curr_r + dy, curr_c + dx
                if not is_within_bounds(next_r, next_c):
                    continue
                if board[next_r][next_c] == "O":
                    queue.append((next_r, next_c))
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"




        # DFS
        # m, n = len(board), len(board[0])
        # def is_within_bounds(row, col):
        #     return 0 <= row < m and 0 <= col < n

        # DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        # def dfs(row, col):
        #     if board[row][col] != "O":
        #         return
            
        #     board[row][col] = "T"
        #     for dy, dx in DIRS:
        #         next_r, next_c = row+dy, col+dx
        #         if not is_within_bounds(next_r, next_c):
        #             continue
        #         if board[next_r][next_c] != 'O':
        #             continue
        #         dfs(next_r, next_c)


        # # DFS from edge, mark T for O cells from an edge
        # # top and bottom row edges
        # for col in range(n):
        #     if board[0][col] == "O":
        #         dfs(0, col)
        #     if board[m - 1][col] == "O":
        #         dfs(m-1, col)
        
        # # left and right col edges
        # for row in range(m):
        #     if board[row][0] == "O":
        #         dfs(row, 0)
        #     if board[row][n - 1] == "O":
        #         dfs(row, n-1)
            
        # for row in range(m):
        #     for col in range(n):
        #         if board[row][col] == "O":
        #             board[row][col] = "X"
        #         elif board[row][col] == "T":
        #             board[row][col] = "O"

