# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        the path from the root of the tree

        root -> node x  == contains no nodes with a value greater than the value of node x
        check node and it is greater than curr max? it is a good node

                3
            3       N
        4       2
        """
        # BFS
        if not root:
            return 0

        queue = deque([(root, float('-inf'))])
        res = 0
        while queue:
            curr_len = len(queue)
            for _ in range(curr_len):
                node, curr_max = queue.popleft()
                if node.val >= curr_max:
                    res += 1
                
                if node.left:
                    queue.append((node.left, max(node.val, curr_max)))
                if node.right:
                    queue.append((node.right, max(node.val, curr_max)))
        return res

        # DFS
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)






