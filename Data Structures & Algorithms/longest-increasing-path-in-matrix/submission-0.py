class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS
        
        def is_within_bounds(row, col):
            return 0 <= row < m and 0 <= col < n

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col):
            if (row, col) not in memo:
                path = 1

                for dy, dx in DIRS:
                    next_r = row + dy
                    next_c = col + dx
                    if is_within_bounds(next_r, next_c)  and matrix[next_r][next_c] > matrix[row][col]:
                        path = max(
                            path,
                            1 + dfs(next_r, next_c)
                        )
                memo[(row, col)] = path
            return memo[(row, col)]
            
        m, n = len(matrix), len(matrix[0])
        memo = {}
        max_len = 1
        for row in range(m):
            for col in range(n):
                max_len = max(max_len, dfs(row, col))        
        return max_len
