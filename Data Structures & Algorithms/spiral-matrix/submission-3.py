class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # left -> right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # top -> bottom
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            # right -> left
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # bottom -> top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
            



        m, n = len(matrix), len(matrix[0])
        res = []

        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return

            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])

            dfs(col, row - 1, r, c, dc, -dr)

        dfs(m, n, 0, -1, 0, 1)
        return res