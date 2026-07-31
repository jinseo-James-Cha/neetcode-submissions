# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                res.append("NULL")
                return
            
            # preorder traversal
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        
        res = []
        dfs(root)
        print(res)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs():
            nonlocal index
            if vals[index] == "NULL":
                index += 1
                return None
            
            node = TreeNode(int(vals[index]))
            index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        vals = data.split(",")
        index = 0
        return dfs()


