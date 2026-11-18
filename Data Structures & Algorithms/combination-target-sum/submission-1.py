class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        distinct integers
        can use multiple times of num
        total == target
        """
        def backtrack(curr, total_sum, idx):
            if total_sum == target:
                res.append(curr[:])
                return
            
            for i in range(idx, len(nums)):
                if nums[i] + total_sum <= target:
                    curr.append(nums[i])
                    backtrack(curr, nums[i] + total_sum, i)
                    curr.pop()
            

        res = []
        nums.sort()
        backtrack([], 0, 0)
        return res