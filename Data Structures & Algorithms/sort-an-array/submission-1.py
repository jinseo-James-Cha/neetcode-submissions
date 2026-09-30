import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Quick sort - avg O(n log n) -> worst O(n^2)
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
    
    def quick_sort(self, nums, start, end):
        if start < end:
            pivot_idx = random.randint(start, end)
            nums[start], nums[pivot_idx] = nums[pivot_idx], nums[start]

            p = self.hoare_partition(nums, start, end)
            self.quick_sort(nums, start, p)
            self.quick_sort(nums, p + 1, end)

    def hoare_partition(self, nums, start, end):
        pivot = nums[start]
        left = start - 1
        right = end + 1

        while True:
            while True:
                left += 1
                if left > end or nums[left] >= pivot:
                    break
            
            while True:
                right -= 1
                if right < start or nums[right] <= pivot:
                    break
            
            if left >= right:
                return right
            
            nums[left], nums[right] = nums[right], nums[left]