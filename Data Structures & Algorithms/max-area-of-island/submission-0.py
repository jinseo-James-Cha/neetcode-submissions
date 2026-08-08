class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # DFS
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col):
            res = 1
            for dy, dx in DIRS:
                next_r, next_c = row + dy, col + dx
                if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                    grid[next_r][next_c] = 0
                    res += dfs(next_r, next_c)
            return res

        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea