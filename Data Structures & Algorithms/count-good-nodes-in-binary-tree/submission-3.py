# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        def dfs(node, maximum):
            nonlocal res
            if not node:
                return
            
            if node.val >= maximum:
                print(node.val)
                res += 1
            
            dfs(node.left, max(maximum, node.val))
            dfs(node.right, max(maximum, node.val))
        res = 0
        dfs(root, float('-inf'))
        return res