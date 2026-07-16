class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two pointers
        nums1_idx = 0
        nums2_idx = 0

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        merged_list = []

        while nums1_idx < nums1_len or nums2_idx < nums2_len:
            curr_num1 = nums1[nums1_idx] if nums1_idx < nums1_len else float('inf')
            curr_num2 = nums2[nums2_idx] if nums2_idx < nums2_len else float('inf')

            if curr_num1 < curr_num2:
                merged_list.append(curr_num1)
                nums1_idx += 1
            else:
                merged_list.append(curr_num2)
                nums2_idx += 1
        print(merged_list)
        
        total_len = len(merged_list)
        half_idx = total_len // 2
        if total_len % 2 == 0:
            return float((merged_list[half_idx - 1] + merged_list[half_idx]) / 2)
        return float(merged_list[half_idx])
