class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two pointers
        # space optimization
        nums1_idx = 0
        nums2_idx = 0

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        med1, med2 = 0, 0
        for _ in range((nums1_len + nums2_len) // 2 + 1):
            med2 = med1
            
            if nums1_idx < nums1_len and nums2_idx < nums2_len:
                if nums1[nums1_idx] < nums2[nums2_idx]:
                    med1 = nums1[nums1_idx]
                    nums1_idx += 1
                else:
                    med1 = nums2[nums2_idx]
                    nums2_idx += 1
            elif nums1_idx < nums1_len:
                med1 = nums1[nums1_idx]
                nums1_idx += 1
            else:
                med1 = nums2[nums2_idx]
                nums2_idx += 1

        
        if (nums1_len + nums2_len) % 2 == 0:
            return float((med1 + med2) / 2)
        return float(med1)

        
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
        
        total_len = len(merged_list)
        half_idx = total_len // 2
        if total_len % 2 == 0:
            return float((merged_list[half_idx - 1] + merged_list[half_idx]) / 2)
        return float(merged_list[half_idx])
