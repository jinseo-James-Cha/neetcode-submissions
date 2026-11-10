# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS
        if not root:
            return True
        
        queue = deque([(root, float('-inf'), float('inf'))])
        while queue:
            curr, minimum, maximum = queue.popleft()
            if not (minimum < curr.val < maximum):
                return False
            
            if curr.left:
                queue.append((curr.left, minimum, curr.val))
            if curr.right:
                queue.append((curr.right, curr.val, maximum))
        return True

        # DFS
        def validateBST(node, maximum, minimum):
            if not node:
                return True
            
            if minimum >= node.val:
                return False
            
            if maximum <= node.val:
                return False
            
            return validateBST(node.left, node.val, minimum) and validateBST(node.right, maximum, node.val)
        
        return validateBST(root.left, root.val, float('-inf')) and validateBST(root.right, float('inf'), root.val)