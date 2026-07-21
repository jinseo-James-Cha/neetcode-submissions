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
        """
        n
        Not Singly linked list -> random linked to any node or NULL

        Deep copy and exactly n node

        """
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
        def copy_node(node):
            if not node:
                return None
            if node in copied:
                return copied[node]
            
            copy = Node(node.val)
            copied[node] = copy
            copy.next = copy_node(node.next)
            copy.random = copy_node(node.random)
            return copy

        copied = {}
        return copy_node(head)