# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left            
            else:
                return cur

        # DFS
        # def dfs(root):
        #     if not root:
        #         return None
            
        #     if root.val == p.val or root.val == q.val:
        #         return root
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     if left and right:
        #         return root
            
        #     return left or right
        
        # return dfs(root)