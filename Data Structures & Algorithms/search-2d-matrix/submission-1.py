class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        ascending order in row and col

        00 01 02 03
        10 11 12 13
        20 21 22 23
        30 31 32 33

        -> in one row
        00 1 2 3 / 4 5 6 7 / 8 9 10 11 / 12 13 14 15
        m*row + col
        """
        # staicase
        # O(m + n)
        m, n = len(matrix), len(matrix[0])
        row = 0
        col = n - 1

        while row < m and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False

        # Binary Search
        # O(log(m * n))
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = (m * n) - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid -1
            else:
                left = mid + 1
        
        return False
        
