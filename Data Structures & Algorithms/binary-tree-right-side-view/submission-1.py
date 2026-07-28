# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # # BFS
        # if not root:
        #     return []
        
        # queue = deque([root])
        # res = []
        # while queue:
        #     last_node_depth = queue[-1]
        #     res.append(last_node_depth.val)
            
        #     curr_len = len(queue)
        #     for _ in range(curr_len):
        #         removed_node = queue.popleft()
        #         if removed_node.left:
        #             queue.append(removed_node.left)
        #         if removed_node.right:
        #             queue.append(removed_node.right)
        # return res

        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        res = []
        dfs(root, 0)
        return res
