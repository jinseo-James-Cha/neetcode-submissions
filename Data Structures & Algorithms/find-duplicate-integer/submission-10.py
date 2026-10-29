class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search
        n = len(nums)
        left = 1
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            lessOrEqual = sum(1 for num in nums if num <= mid)
            if lessOrEqual <= mid:
                left = mid + 1
            else:
                right = mid
        return left
        
        # without modifying array
        # O(n) + O(n)
        check = [False] * (len(nums) + 1)
        for num in nums:
            if check[num]:
                return num
            check[num] = True
        return -1

        # sort
        # O(n log n) + O(1)
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                return nums[i]
        return -1

        # brute force - hashset
        # O(n) and O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1