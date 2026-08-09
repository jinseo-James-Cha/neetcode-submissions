class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        -1 : water 
        0 : treasure
        INF: land

        traversed up, down, left, or right.
        Modify the grid in-place.
        """
        m, n = len(grid), len(grid[0])
        INF = 2**31 - 1

        queue = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dy, dx in DIRS:
                next_r, next_c = row + dy, col + dx

                if not (0 <= next_r < m and 0 <= next_c < n):
                    continue

                if grid[next_r][next_c] != INF:
                    continue

                grid[next_r][next_c] = grid[row][col] + 1
                queue.append((next_r, next_c))
            

        # DFS
        # m, n = len(grid), len(grid[0])

        # def is_within_bounds(row, col):
        #     return 0 <= row < m and 0 <= col < n

        # DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        # INF = 2**31 - 1
        # def dfs(row, col, distance):
        #     grid[row][col] = distance

        #     for dy, dx in DIRS:
        #         next_r, next_c = row + dy, col + dx
        #         if is_within_bounds(next_r, next_c):
        #             if grid[next_r][next_c] == 0 or grid[next_r][next_c ] == -1:
        #                 continue
        #             elif grid[next_r][next_c] > distance:
        #                 dfs(next_r, next_c, distance + 1)
                    


        # for row in range(m):
        #     for col in range(n):
        #         if grid[row][col] == 0:
        #             dfs(row, col, 0)


