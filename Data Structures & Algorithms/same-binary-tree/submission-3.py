# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # BFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            if p.left or q.left:
                queue.append((p.left, q.left))
            if p.right or q.right:
                queue.append((p.right, q.right))
        
        return True


    # DFS
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
        
    #     if not p or not q:
    #         return False
        
    #     if p.val != q.val:
    #         return False
        
    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)