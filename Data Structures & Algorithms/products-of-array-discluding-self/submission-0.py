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

        # from Left to Right
        n = len(nums)
        res = [1] * n
        
        from_left = nums[0]
        for i in range(1, n):
            res[i] = from_left
            from_left *= nums[i]
        
        from_right = nums[-1]
        for i in range(n-2, -1, -1):
            res[i] *= from_right
            from_right *= nums[i]
        return res

