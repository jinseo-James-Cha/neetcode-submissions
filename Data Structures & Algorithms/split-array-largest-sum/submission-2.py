class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = num
            return True
            
        # binary search
        left = max(nums)
        right = sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if canSplit(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


        # dp topdown = dfs + memoization
        n = len(nums)

        def dfs(i, m):
            if i == n:
                return 0 if m == 0 else float('inf')
            if m == 0:
                return float('inf')
            
            if (i, m) not in memo:
                res = float('inf')
                curSum = 0
                for j in range(i, n - m + 1):
                    curSum += nums[j]
                    res = min(res, max(curSum, dfs(j + 1, m - 1)))      
                memo[(i, m)] = res
            
            return memo[(i, m)]
        memo = {}
        return dfs(0, k)