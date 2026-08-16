import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        weighted(0 < weight) edge graph
        shortest path from 0,0 to n-1,n-1
        
        A path from 0,0 to n-1,n-1, but maximum number

        choose minimum num in a position and save its maximum
        """

        # dijkstra
        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        N = len(grid)
        min_heap = [(grid[0][0], 0, 0)]
        visited = {(0,0)}
        res = grid[0][0]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == N - 1 and c == N - 1:
                return t
            
            for dy, dx in DIRS:
                next_r, next_c = r + dy, c + dx
                if not is_within_bounds(next_r, next_c):
                    continue
                if (next_r, next_c ) in visited:
                    continue
                
                visited.add((next_r, next_c))
                heapq.heappush(min_heap, (max(t, grid[next_r][next_c]), next_r, next_c))
        
        return -1




