from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Topological sort(kahn's algorithm)
        m, n = len(matrix), len(matrix[0])
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        indegree = [[0] * n for _ in range(m)]

        def is_within_bounds(row, col):
            return 0 <= row < m and 0 <= col < n

        for row in range(m):
            for col in range(n):
                for dy, dx in DIRS:
                    nr, nc = row + dy, col + dx
                    if is_within_bounds(nr, nc) and matrix[row][col] > matrix[nr][nc]:
                        indegree[row][col] += 1
        
        queue = deque()
        for row in range(m):
            for col in range(n):
                if indegree[row][col] == 0:
                    queue.append((row, col))
        
        max_path = 0
        while queue:
            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()
                for dy, dx in DIRS:
                    nr, nc = curr_r + dy, curr_c + dx
                    if is_within_bounds(nr, nc) and matrix[curr_r][curr_c] < matrix[nr][nc]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            queue.append((nr, nc))
            max_path += 1
        return max_path

        
        # DP - top down 
        def is_within_bounds(row, col):
            return 0 <= row < m and 0 <= col < n

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dp(row, col):
            if (row, col) not in memo:
                path = 1

                for dy, dx in DIRS:
                    next_r = row + dy
                    next_c = col + dx
                    if is_within_bounds(next_r, next_c)  and matrix[next_r][next_c] > matrix[row][col]:
                        path = max(
                            path,
                            1 + dp(next_r, next_c)
                        )
                memo[(row, col)] = path
            return memo[(row, col)]

        m, n = len(matrix), len(matrix[0])
        memo = {}
        max_len = 1
        for row in range(m):
            for col in range(n):
                max_len = max(max_len, dp(row, col))        
        return max_len
