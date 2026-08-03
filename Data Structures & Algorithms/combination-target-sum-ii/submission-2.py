class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, remaining, start):
            if remaining == 0:
                res.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > remaining:
                    continue
                
                curr.append(candidates[i])
                backtrack(curr, remaining - candidates[i], i+1)
                curr.pop()
        
        res = []
        candidates.sort()
        backtrack([], target, 0)
        return res
