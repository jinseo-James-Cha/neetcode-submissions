# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        entry root
        """
        # DP
        cache = { None: 0}
        def dfs(root):
            if root in cache:
                return cache[root]
            
            cache[root] = root.val
            if root.left:
                cache[root] += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                cache[root] += dfs(root.right.left) + dfs(root.right.right)
            
            cache[root] = max(cache[root], dfs(root.left) + dfs(root.right))
            return cache[root]
        return dfs(root)

        # DFS 
        if not root:
            return 0

        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)
        
        res = max(res, self.rob(root.left) + self.rob(root.right))
        return res
            