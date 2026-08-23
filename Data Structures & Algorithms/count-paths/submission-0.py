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
        dp = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[m-1][n-1]