# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
                    -15
        10              20
                    15      5
                -5

        
                15
        10              40
                    15      5
                -5      

                1
            2       
        3   
    4
5
        """
        def dfs(node):
            nonlocal max_sum
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            total = node.val
            total += left if left > 0 else 0
            total += right if right > 0 else 0
            max_sum = max(max_sum, total)
            return node.val + max(0, left, right)        
        max_sum = float('-inf')
        dfs(root)
        return max_sum











