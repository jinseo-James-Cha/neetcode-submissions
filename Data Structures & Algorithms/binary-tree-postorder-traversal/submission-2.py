# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                curr = curr.left
        res.reverse()
        return res
        



        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        
        res = []
        dfs(root)
        return res