class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1 2 3 4 5 6 7 8 and k = 4
        0 1 2 3 4 5 6 7
        
        -> rotate
        8 1 2 3 4 5 6 7

        """
        
        n = len(nums)
        if k == 0 or k % n == 0:
            return
        
        k %= n

        while k:
            curr_last = nums[-1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = curr_last
            k -= 1
        