class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        burst all of the balloons = n

        idx -1 0 1 2 n n+1
        val  1 4 2 3 7 1 -> out of n range value is 1

        burst ith balloon = nums[i - 1] * nums[i] * nums[i + 1]

        return the maximum number
        """
        # DP - bottom up
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]

        # DP - Top down - TLE
        nums = [1] + nums + [1]
        memo = {}
        def dp(left, right):
            if left > right:
                return 0
            
            if (left, right) not in memo:
                max_res = 0
                for i in range(left, right + 1):
                    coins = nums[left - 1] * nums[i] * nums[right + 1]
                    coins += dp(left, i - 1) + dp(i + 1, right)
                    max_res = max(max_res, coins)
                memo[(left, right)] = max_res
            
            return memo[(left, right)]

        return dp(1, len(nums) - 2)
