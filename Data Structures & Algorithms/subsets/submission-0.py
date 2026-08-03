class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        unique combinations

                    []
            1       2       3
        2       3       3       
    3       
        """
        # backtracking

        def backtrack(curr, start):
            res.append(curr[:])
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        
        res = []
        backtrack([], 0)
        return res