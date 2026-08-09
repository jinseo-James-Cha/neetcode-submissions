"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if node in copied_node:
                return copied_node[node]
            
            new_copy = Node(node.val)
            copied_node[node] = new_copy
            for neighbor in node.neighbors:
                new_copy.neighbors.append(dfs(neighbor))
            
            return new_copy
        
        copied_node = {}
        return dfs(node) if node else None
