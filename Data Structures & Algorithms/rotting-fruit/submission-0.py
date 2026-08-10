from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        0 : empty
        1 : fresh fruit
        2 : rotton fruit
        """

        # BFS
        m, n = len(grid), len(grid[0])
        def is_within_bounds(row, col):
            return 0 <= row < m and 0 <= col < n

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        
        # set up rotton fruit as default
        fresh_fruit = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_fruit += 1
        
        min_minute = 0
        flag = False
        while queue and fresh_fruit > 0:
            curr_len = len(queue)
            for _ in range(curr_len):
                curr_row, curr_col = queue.popleft()
                for dy, dx in DIRS:
                    next_row, next_col = curr_row + dy, curr_col + dx
                    if is_within_bounds(next_row, next_col) and grid[next_row][next_col] == 1:
                        flag = True
                        grid[next_row][next_col] = 2
                        fresh_fruit -= 1
                        queue.append((next_row, next_col))

            min_minute += 1

        return min_minute if fresh_fruit == 0 else -1




