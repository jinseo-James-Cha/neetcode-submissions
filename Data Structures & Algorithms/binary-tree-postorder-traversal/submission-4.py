# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris
        res = []
        curr = root
        while curr:
            if not curr.right:
                res.append(curr.val)
                curr = curr.left
            else:
                prev = curr.right
                while prev.left and prev.left != curr:
                    prev = prev.left
                
                if not prev.left:
                    res.append(curr.val)
                    prev.left = curr
                    curr = curr.right
                else:
                    prev.left = None
                    curr = curr.left
        res.reverse()
        return res



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