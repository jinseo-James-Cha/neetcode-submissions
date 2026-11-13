# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        -5 ? yes this is maximum for now
        15 ? yes without child this is the maximum
        
        5 ? yes this is maximum

        20 ? itself or all together with children? or left only or rightonly?

        -5 일때 -5, -inf -inf and two more.. => -5
        15일때 15, -5, -inf, 10, and.. => 15
        5 일때 5, ... => 5

        20일때 20, 35, 25, 35 + 25 - 20=40
        """
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            res = max(res, node.val + left + right)

            return node.val + max(left, right)

        res = float('-inf')
        dfs(root)
        return res



