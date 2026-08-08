class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"
            
            while queue:
                row, col = queue.popleft()

                for dy, dx in DIRS:
                    next_r, next_c = row + dy, col + dx
                    if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == "1":
                        grid[next_r][next_c] = "0"
                        queue.append((next_r, next_c))
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    bfs(row, col)
        return res
        
        # DFS
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col):
            grid[row][col] = "0"

            for dy, dx in DIRS:
                next_r, next_c = row + dy, col + dx
                if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == "1":
                    dfs(next_r, next_c)
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    dfs(row, col)
        return res