class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
                            []
                        1   2   1
                    2       
                1   
        """
        # def backtrack(curr, start):            
        #     res.append(curr[:])
                
        #     for i in range(start, len(nums)):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         curr.append(nums[i])
        #         backtrack(curr, i+1)
        #         curr.pop()

        # nums.sort()
        # res = []
        # backtrack([],0)
        # return res


        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)

        res = set()
        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]