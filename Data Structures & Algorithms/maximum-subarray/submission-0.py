class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        subarray with the largest sum
        subarray? sum? kadane's algorithm?
        """

        largest_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            largest_sum = max(largest_sum, curr_sum)
        return largest_sum