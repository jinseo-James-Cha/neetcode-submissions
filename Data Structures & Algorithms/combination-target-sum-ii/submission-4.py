class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        unique combination
        any order of combinations
        any order in a combination
        an element is chosen once
        """

        def backtrack(curr, idx, ramaining):
            if ramaining == 0:
                res.append(curr[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i]> ramaining:
                    continue
                
                curr.append(candidates[i])
                backtrack(curr, i + 1, ramaining - candidates[i])
                curr.pop()

        candidates.sort()
        res = []
        backtrack([], 0, target)
        return res