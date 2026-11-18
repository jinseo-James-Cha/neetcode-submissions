class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Unique integers
        no duplicates
        """

        def backtrack(curr, idx):
            tuple_curr = tuple(curr)
            if tuple_curr not in seen:
                res.append(curr[:])
                seen.add(tuple_curr)
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        res = []
        seen = set()
        backtrack([], 0)
        return res