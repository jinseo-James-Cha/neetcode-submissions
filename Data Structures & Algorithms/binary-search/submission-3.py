class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        distinct integers, sorted in ascending order
        find target's index or return -1
        """

        # binary search - O(log n)
        left = 0
        right = len(nums) - 1
        while left <= right:
            # mid = (left + right) // 2
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

        # brute force - O(n)
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1