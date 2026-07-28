# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST
        # BFS
        if not root:
            return True
        
        queue = deque([(root, float('inf'), float('-inf'))])
        while queue:
            node, maximum, minimum = queue.popleft()
            if node.val >= maximum:
                return False
            if node.val <= minimum:
                return False
            
            if node.left:
                queue.append((node.left, node.val, minimum))
            if node.right:
                queue.append((node.right, maximum, node.val))
        return True
        
        # BST
        # DFS
        if not root:
            return True
        
        def isValid(node, maximum, minimum):
            if not node:
                return True
            
            if node.val >= maximum:
                return False
            
            if node.val <= minimum:
                return False
            
            return isValid(node.left, node.val, minimum) and isValid(node.right, maximum, node.val)

        return isValid(root.left, root.val, float('-inf')) and isValid(root.right, float('inf'), root.val)
