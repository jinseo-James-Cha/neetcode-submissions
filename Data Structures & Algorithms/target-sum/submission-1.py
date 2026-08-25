from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DP - Bottom up
        # range -6 ~ +6
        n = len(nums)
        total_sum = sum(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count
        return dp[n][target]



        # DP - top down
        def dp(idx, remaining):
            if idx == len(nums):
                if remaining == 0:
                    return 1
                return 0
            
            if (idx, remaining) not in memo:
                res = dp(idx+1, remaining + nums[idx])
                res += dp(idx+1, remaining - nums[idx])
                memo[(idx, remaining)] = res
            return memo[(idx, remaining)]
        
        memo = {}
        return dp(0, target)