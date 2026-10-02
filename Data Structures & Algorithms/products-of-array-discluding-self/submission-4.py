class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 2 4 6
        index based calculations
        0: 1R* 2R * 3R
        1: 0L * 2R * 3R
        2: 0L * 1L * 3R
        3: 0L * 1L * 2L
        """
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

        
