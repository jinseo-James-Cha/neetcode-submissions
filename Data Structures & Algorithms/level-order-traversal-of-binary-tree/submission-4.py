# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if not root:
            return []
        queue = deque([root])

        res = []
        while queue:
            curr_len = len(queue)
            curr_res = []
            for _ in range(curr_len):
                curr = queue.popleft()
                curr_res.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr_res[:])
        return res


        # DFS
        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)



        
        res = []
        dfs(root, 0)
        return res