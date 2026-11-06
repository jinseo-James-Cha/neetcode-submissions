# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        BST
        """
        if not root:
            return root
        
        parent = None
        curr = root
        while curr and curr.val != key:
            parent = curr
            if curr.val < key:
                curr = curr.right
            else:
                curr = curr.left
        
        # not found
        if not curr:
            return root
        
        # found, but one side child
        if not curr.left or not curr.right:
            child = curr.left or curr.right
            if not parent:
                return child
            
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else:
            # found node with both side child
            par = None
            delNode = curr
            curr = curr.right
            while curr.left:
                par = curr
                curr = curr.left

            if par:
                par.left = curr.right
                curr.right = delNode.right
            
            curr.left = delNode.left

            if not parent:
                return curr
            
            if parent.left == delNode:
                parent.left = curr
            else:
                parent.right = curr
        return root


        # curr = root
        # while curr:
        #     if curr.val < key:
        #         curr = curr.right
        #     elif curr.val > key:
        #         curr = curr.left
        #     else:
        #         if curr.left:
        #             temp = curr.right
        #             curr = curr.left
        #             curr.right = temp
        #         elif curr.right:
        #             temp = curr.left
        #             curr = curr.right
        #             curr.left = temp
        # return root