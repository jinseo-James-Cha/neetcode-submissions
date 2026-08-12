from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        0 : 1 2 3
        1 : 0 4
        2 : 0
        3 : 0
        4 : 1

        """
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