class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        sorted num and skip the same number in the same level
        """
        def backtrack(curr, start):
            res.append(curr[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                    
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()

        res = []
        nums.sort()
        backtrack([], 0)
        return res