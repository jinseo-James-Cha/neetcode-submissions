class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
                            []
                        1   2   1
                    2       
                1   
        """
        def backtrack(curr, start):            
            res.append(curr[:])
                
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()

        nums.sort()
        res = []
        backtrack([],0)
        return res


        def backtrack(curr, start):
            tuple_combination = tuple(curr)
            if tuple_combination in seen:
                return
            
            seen.add(tuple_combination)
            res.append(curr[:])
                
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
            
        res = []
        seen = set()
        backtrack([], 0)
        return res