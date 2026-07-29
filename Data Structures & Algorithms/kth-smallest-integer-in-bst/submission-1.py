# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder, dfs
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        res = []
        dfs(root)
        return res[k-1]
        
        # brute force
        # dfs
        def dfs(node):
            if not node:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        res.sort()
        return res[k-1]