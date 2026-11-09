# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS
        if not root:
            return 0
        
        queue = deque([(root, float('-inf'))])
        res = 0
        while queue:
            for _ in range(len(queue)):
                curr, prev_max = queue.popleft()
                if curr.val >= prev_max:
                    res += 1
                
                curr_max = max(curr.val, prev_max)
                if curr.left:
                    queue.append((curr.left, curr_max))
                if curr.right:
                    queue.append((curr.right, curr_max))
        return res
        
        
        # DFS
        def dfs(node, maximum):
            nonlocal res
            if not node:
                return
            
            if node.val >= maximum:
                res += 1
            
            dfs(node.left, max(maximum, node.val))
            dfs(node.right, max(maximum, node.val))
        res = 0
        dfs(root, float('-inf'))
        return res