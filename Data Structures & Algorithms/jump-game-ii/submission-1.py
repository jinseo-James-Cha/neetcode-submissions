class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        val 2 4 1 1 1 1
        idx 0 1 2 3 4 5
            -         H
        max_idx = 2
        jump 1
        """

        if len(nums) == 1:
            return 0
        
        total_max = nums[0]
        curr_max = nums[0]
        num_of_jump = 1
        for i in range(1, len(nums)-1):
            total_max = max(total_max, i + nums[i])
            if curr_max <= i:
                curr_max = total_max
                num_of_jump += 1
        
        return num_of_jump
