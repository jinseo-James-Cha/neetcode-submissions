# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # BFS
        if not root:
            return 0
        stack = [(root, 1)]
        maximum_depth = 1
        while stack:
            node, depth = stack.pop()
            maximum_depth = max(maximum_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return maximum_depth
        
        # DFS
        def dfs(root):
            if not root:
                return 0
            
            return max(dfs(root.left), dfs(root.right)) + 1
        return dfs(root)