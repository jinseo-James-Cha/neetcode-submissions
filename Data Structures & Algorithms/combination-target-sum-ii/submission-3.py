class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        unique combination
        any order of combinations
        any order in a combination
        an element is chosen once
        """

        def backtrack(curr, idx, total):
            if total == target:
                res.append(curr[:])
                return
            
            if total > target or idx == len(candidates):
                return
            
            curr.append(candidates[idx])
            backtrack(curr, idx + 1, total + candidates[idx])
            curr.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(curr, idx + 1, total)

        candidates.sort()
        res = []
        backtrack([], 0, 0)
        return res