class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Ascending order
        1,2,3,4,5,6

            3 4 5 6 1 2 3 -> 4 times rotated
        1 2 3 4 5 6 -> 6 times rotated -> the same as original

        minimum rotate 1
        maximum rotate n
        
        return the minimum element

        """
        n = len(nums)
        left = 0
        right = n - 1
        res = nums[0]
        while left <= right:
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res







