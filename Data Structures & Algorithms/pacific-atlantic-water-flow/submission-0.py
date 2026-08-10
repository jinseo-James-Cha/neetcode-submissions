class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        top left : pacific ocean
        bottom right : altantic ocean

        directions: up down left right
        can move height equal or lower
        """
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def is_within_bounds(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            
            visited.add((row, col))

            for dy, dx in DIRS:
                next_r, next_c = row + dy, col + dx
                if not is_within_bounds(next_r, next_c):
                    continue
                if (next_r, next_c) in visited:
                    continue
                if heights[next_r][next_c] < heights[row][col]:
                    continue
                
                dfs(next_r, next_c, visited)


        # top - pacific and bottom - atlantic rows
        for col in range(n):
            dfs(0, col, pacific)
            dfs(m-1, col, atlantic)
        
        for row in range(m):
            dfs(row, 0, pacific)
            dfs(row, n-1, atlantic)
        
        res = []
        for row in range(m):
            for col in range(n):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res


        