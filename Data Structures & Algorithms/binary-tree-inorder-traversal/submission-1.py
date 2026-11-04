# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # BFS inorder
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


        # DFS inorder 
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
            
        
        res = []
        dfs(root)
        return res
