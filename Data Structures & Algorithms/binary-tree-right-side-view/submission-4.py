# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        if not root:
            return []
            
        queue = deque([root])
        res = []
        while queue:
            most_right = None
            for _ in range(len(queue)):
                curr = queue.popleft()
                most_right = curr

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(most_right.val)
        return res

        # DFS
        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append(node.val)
            else:
                res[depth] = node.val
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        res = []
        dfs(root, 0)
        return res