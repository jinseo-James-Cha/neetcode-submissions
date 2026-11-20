class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        res len == nums len
        index combinations..
        """
        res, n = [], len(nums)
        visit = [False] * n

        def dfs(curr):
            if len(curr) == n:
                res.append(curr[:])
                return

            for i in range(n):
                if visit[i]:
                    continue

                if i and nums[i] == nums[i - 1] and not visit[i - 1]:
                    continue
                visit[i] = True
                curr.append(nums[i])
                dfs(curr)
                visit[i] = False
                curr.pop()

        nums.sort()
        dfs([])
        return res


        def backtrack(curr, used_idx):
            if len(curr) == len(nums):
                tuple_curr = tuple(curr)
                if tuple_curr not in seen:
                    res.append(curr[:])
                    seen.add(tuple_curr)
                return
            
            for i in range(len(nums)):
                if i not in used_idx:
                    curr.append(nums[i])
                    used_idx.add(i)

                    backtrack(curr, used_idx)

                    curr.pop()
                    used_idx.remove(i)
        
        res = []
        seen = set()
        backtrack([], set())
        return res