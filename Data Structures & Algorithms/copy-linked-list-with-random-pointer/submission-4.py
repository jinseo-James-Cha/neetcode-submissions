"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # BFS
        copied = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copied[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copied[curr]
            copy.next = copied[curr.next]
            copy.random = copied[curr.random]
            curr = curr.next
        return copied[head]
        
        # DFS
        def dfs(node):
            if not node:
                return None
            if node in copies:
                return copies[node]
            
            # create copy node
            copy_node = Node(node.val)
            copies[node] = copy_node
            copy_node.next = dfs(node.next)
            copy_node.random = dfs(node.random)
            return copy_node

        copies = {}
        return dfs(head)