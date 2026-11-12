# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # iterative 
        stack = [root]
        visit = set()
        parents = {root: None}
        
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]
                    if not p:
                        return None
                    elif p.left == node:
                        p.left = None
                    elif p.right == node:
                        p.right = None
            elif node not in visit:
                visit.add(node)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node
        return root

        # DFS
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

        # DFS
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root