class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        find combination which total sum is equal to target
        """
        def backtrack(curr, remaining ,start_idx):
            if start_idx == len(nums):
                return
            
            if remaining == 0:
                res.append(curr[:])
                return
            
            for i in range(start_idx, len(nums)):
                if remaining - nums[i] >= 0:
                    curr.append(nums[i])
                    backtrack(curr, remaining - nums[i], i)
                    curr.pop() 



        res = []
        backtrack([], target ,0)
        return res