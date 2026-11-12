# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(root):
            if root in cache:
                return cache[root]
            
            res = root.val
            if root.left:
                res += dp(root.left.left) + dp(root.left.right)
            if root.right:
                res += dp(root.right.left) + dp(root.right.right)
            
            cache[root] = max(res, dp(root.left) + dp(root.right))
            return cache[root]

        # DP
        cache = {None: 0}
        return dp(root)