class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        3P3= 3 * 2 * 1 = 6
        """

        def backtrack(curr, used):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if i not in used:
                    curr.append(nums[i])
                    used.add(i)

                    backtrack(curr, used)

                    curr.pop()
                    used.remove(i)
        res = []
        backtrack([], set())
        return res