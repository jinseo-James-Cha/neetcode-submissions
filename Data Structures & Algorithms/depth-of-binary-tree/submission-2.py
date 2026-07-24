# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        max_depth = 0
        while queue:
            curr_len = len(queue)
            for _ in range(curr_len):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            max_depth += 1
            
        return max_depth


    # DFS
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
        
    #     left_depth = self.maxDepth(root.left) + 1
    #     right_depth = self.maxDepth(root.right) + 1
    #     return max(left_depth, right_depth)