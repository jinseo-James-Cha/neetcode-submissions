import heapq

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset, yset = self.find(x), self.find(y)
        if xset == yset:
            return False
        
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        weighted(0 < weight) edge graph
        shortest path from 0,0 to n-1,n-1
        
        A path from 0,0 to n-1,n-1, but maximum number

        choose minimum num in a position and save its maximum
        """
        # Kruskal
        N = len(grid)
        uf = UnionFind(N * N)
        edges = []
        for r in range(N):
            for c in range(N):
                edges.append((grid[r][c], r, c))
        edges.sort()

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for t, r, c in edges:
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if is_within_bounds(nr, nc) and grid[nr][nc] <= t:
                    uf.union(r * N + c, nr * N + nc)
                
            if uf.connected(0, N * N - 1):
                return t
        return -1


        # dijkstra
        # def is_within_bounds(row, col):
        #     return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        # N = len(grid)
        # min_heap = [(grid[0][0], 0, 0)]
        # visited = {(0,0)}
        # DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        # while min_heap:
        #     t, r, c = heapq.heappop(min_heap)
        #     if r == N - 1 and c == N - 1:
        #         return t
            
        #     for dy, dx in DIRS:
        #         next_r, next_c = r + dy, c + dx
        #         if not is_within_bounds(next_r, next_c):
        #             continue
        #         if (next_r, next_c ) in visited:
        #             continue
                
        #         visited.add((next_r, next_c))
        #         heapq.heappush(min_heap, (max(t, grid[next_r][next_c]), next_r, next_c))
        
        # return -1




