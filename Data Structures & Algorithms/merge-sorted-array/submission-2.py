class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        10 20 20 40 0 0 m = 4
        1  2            n = 2

        len(nums1) = m + n
        order the merged list in ascending order
        """
        last = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            last -= 1



        # merge in reverse order
        # curr_last = m + n - 1
        # while 0 < m and 0 < n:
        #     if nums1[m-1] > nums2[n-1]:
        #         nums1[curr_last] = nums1[m-1]
        #         m -= 1
        #     else:
        #         nums1[curr_last] = nums2[n - 1]
        #         n -= 1
        #     curr_last -= 1
        
        # while 0 < n:
        #     nums1[curr_last] = nums2[n - 1]
        #     n -= 1
        #     curr_last -= 1
        
