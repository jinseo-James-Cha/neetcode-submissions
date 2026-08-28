class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        can reach the last index from 0 index?

        idx 0 1 2 3 4
        val 1 2 0 1 0
            - -   - - True

        idx 0 1 2 3 4
        val 1 2 0 1 0

        idx 0 1 2 3 4
        val 1 2 0 1 0

        curr_max = 1          
        """
        n = len(nums)
        if n == 1:
            return True
        
        if nums[0] == 0:
            return False
        
        curr_max = nums[0]
        for i in range(1, n):
            if curr_max < i:
                return False
            
            curr_max = max(curr_max, i + nums[i])
        return curr_max >= n-1