class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        distinct integers
        ascending order

        -1,0,2,4,6,8
        L          R
               M
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1