# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root, p, q):
            nonlocal lca
            if not root:
                return 0
            
            from_left = dfs(root.left, p, q)
            from_right = dfs(root.right, p, q)
            myself = 1 if root.val == p.val or root.val == q.val else 0

            total = from_left + from_right + myself
            if total >= 2 and lca is None:
                lca = root
            return total
                  
        lca = None
        dfs(root, p, q)
        return lca