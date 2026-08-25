class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
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