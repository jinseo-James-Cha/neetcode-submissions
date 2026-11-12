# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return [True, None]
            
            is_left_leaf, left_node = dfs(node.left)
            is_right_leaf, right_node = dfs(node.right)
            if is_left_leaf and is_right_leaf and node.val == target:
                return [True, None]
            
            node.left = left_node
            node.right = right_node
            return [False, node]
        
        return dfs(root)[1]

        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root