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


        1 2 3 4 5 6 7 8 + 1 2 3 4 5 6 7 8
        0 1 2 3 4 5 6 7   8 9 10 11 12 13 14 15
                - - - -   - - - -


        reverse
        8 7 6 5 4 3 2 1
        reverse k and + k ~ n-1
        5 6 7 8 + 1 2 3 4
        """
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        
        # Brute force
        # n = len(nums)
        # if k == 0 or k % n == 0:
        #     return
        
        # k %= n

        # while k:
        #     curr_last = nums[-1]
        #     for i in range(n - 1, 0, -1):
        #         nums[i] = nums[i - 1]
        #     nums[0] = curr_last
        #     k -= 1
        