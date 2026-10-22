class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1 2 4 8
        10 11 12 13
        14 20 30 40

        1 2 4 8     10 11 12 13     14 20 30 40
        0 1 2 3      4 5  6  7      8  9  10 11
        
        row * col + col
        """
        m,n = len(matrix), len(matrix[0])
        
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False