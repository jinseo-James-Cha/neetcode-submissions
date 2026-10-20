class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        return lower bound index which means equal to or less
        """
        n = len(nums)
        left = 0
        right = n
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left