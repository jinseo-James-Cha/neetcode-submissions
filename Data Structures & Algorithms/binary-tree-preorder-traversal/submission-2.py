# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # BFS
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res


        # DFS
        def dfs(root):
            if not root:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
            
        res = []
        dfs(root)
        return res