class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        if max(nums) > total // k:
            return False
        
        sides = [total // k] * k
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True
            
            for side in range(k):
                if sides[side] - nums[i] >= 0:
                    sides[side] -= nums[i]
                    if dfs(i + 1):
                        return True
                    sides[side] += nums[i]
                
                if sides[side] == total // k:
                    break
            
            return False

        return dfs(0)