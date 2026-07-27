# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS
        def dfs(root, depth):
            if not root:
                return
            
            if len(res) == depth:
                res.append([])
            
            res[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            
        res = []
        dfs(root, 0)
        return res

        # BFS
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            curr = []
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr[:])
        return res
