"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        n * n grid
        0 or 1 in integers

        grid -> Quad-Tree grid. and return the root. prob 0,0

        Quad-Tree
        - val -> True for 1 False for 0, when isLeaf is False
        - isLeaf -> True if a leaf node and False if the node has four children

        TL   TR
        BL.  BR
        """
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c], True)

            n = n // 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c + n)
            bottomleft = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)