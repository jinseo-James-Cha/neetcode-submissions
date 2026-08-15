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

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        - undirected edges
        - manhattan distance = |xi - xj| + |yi - yj|
        - return minimum cost to connect all points
        - only one path
        => Minimum Spanning Tree(MST)
    
        """
        n = len(points)
        uf = UnionFind(n)
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                manhattan_distance = abs(xi - xj) + abs(yi - yj)
                edges.append((manhattan_distance, i, j))
        
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if uf.union(u,v):
                res += dist
        return res







