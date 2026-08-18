class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        going through all possibilities until the end
        mind maximum amount

        n = len(nums)

        max = n-1 + nums[n-1] or n-2 + nums[n-2]
        """
        # DP - bottom up
        n = len(nums)
        if n <= 2:
            return max(nums[:n])
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]


        # DP - top down
        n = len(nums)
        def dp(i):
            if i == 0:
                return nums[0] 
            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in memo:
                one_back = dp(i-1)
                two_back = dp(i-2) + nums[i]
                memo[i] = max(one_back, two_back)
            return memo[i]

        memo = {}
        return dp(n-1)
