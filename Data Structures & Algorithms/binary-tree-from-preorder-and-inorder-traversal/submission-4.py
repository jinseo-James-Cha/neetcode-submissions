# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder + inorder = binary tree
        1 2 3 4.   2 1 3 4

        preorder's first one is the head
        so its index is 1 in inorder
        if left of the index is left tree and right side is the right tree
        """
        # hashmap
        indices = {}
        for idx, val in enumerate(inorder):
            indices[val] = idx
        
        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            
            
            root_val = preorder[pre_idx]
            pre_idx += 1
            
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        pre_idx = 0
        return dfs(0, len(inorder) - 1)




        # DFS - o(n^2) -> TLE
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root