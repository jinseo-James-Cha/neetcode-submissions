class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Unique integers
        no duplicates
        """

        def backtrack(curr, idx):
            res.append(curr[:])
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        res = []
        backtrack([], 0)
        return res