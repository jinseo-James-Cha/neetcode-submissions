from collections import defaultdict, deque

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        0 : 1 2 3
        1 : 0 4
        2 : 0
        3 : 0
        4 : 1

        """
        # Union Find
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for u,v in edges:
            if not uf.union(u,v):
                return False
        return True
        




        # BFS
        if len(edges) > n - 1:
            return False
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        queue = deque([(0, -1)])
        visited.add(0)
        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                queue.append((neighbor, node))
        return len(visited) == n
    

        # DFS
        if len(edges) > n - 1:
            return False
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == par:
                    continue
                
                if not dfs(neighbor, node):
                    return False
            return True

        visited = set()
        return dfs(0, -1) and len(visited) == n