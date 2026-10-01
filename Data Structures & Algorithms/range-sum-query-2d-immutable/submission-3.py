class NumMatrix:
    """
    I think this would be a prefix sum question.
    let me think as it is array instead of Matrix.
    """
    # 2D Prefix sum for rows and cols
    # bottomRight - above - left + topLeft
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft

    # 1D prefix sum for rows
    # def __init__(self, matrix: List[List[int]]):
    #     self.prefixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    #     for row in range(len(matrix)):
    #         self.prefixSum[row][0] = matrix[row][0]
    #         for col in range(1, len(matrix[0])):
    #             self.prefixSum[row][col] = self.prefixSum[row][col-1] + matrix[row][col]

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     res = 0
    #     for row in range(row1, row2 + 1):
    #         if col1 > 0:
    #             res += self.prefixSum[row][col2] - self.prefixSum[row][col1 - 1]
    #         else:
    #             res += self.prefixSum[row][col2]
    #     return res

    # This is brute force solution
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix
        

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     total_sum = 0
    #     for row in range(row1, row2 + 1):
    #         for col in range(col1, col2 + 1):
    #             total_sum += self.matrix[row][col]
    #     return total_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)