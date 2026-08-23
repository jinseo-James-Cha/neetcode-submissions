class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        start 0,0 
        end m-1, n-1

        can move right or down..
        00 -> -> ->
        |  2   3  4
        |
        |
        """
        # DP - Bottom up - space optimization
        prev_row = [1] * n
        for row in range(1, m):
            curr_row = [1] * n
            for col in range(1, n):
                curr_row[col] = prev_row[col] + curr_row[col-1]
            prev_row = curr_row
        return prev_row[n-1]

        # DP - bottom up
        dp = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[m-1][n-1]

        # DP - top down
        def dp(row, col):
            if row == 0 or col == 0:
                return 1
            
            if (row, col) not in memo:
                memo[(row,col)] = dp(row-1, col) + dp(row, col-1)
            return memo[(row, col)]
        memo = {}
        return dp(m-1, n-1)



