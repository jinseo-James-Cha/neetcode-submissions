# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BFS
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
        


        # DFS
        def dfs(node):
            nonlocal res

            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            myself = p.val == node.val or q.val == node.val

            if left + right + myself >= 2:
                res = node
        
            return left or right or myself
        
        res = None
        dfs(root)
        return res