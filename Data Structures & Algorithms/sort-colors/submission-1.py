import random
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in-place sort -> quick sort, heap sort
        self.heap_sort(nums)

        # Quick sort randomized(pivot)
        # self.quick_sort(nums, 0, len(nums) - 1)
    def heap_sort(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i, nums)
        
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(i, 0, nums)

    def heapify(self, heap_size, idx, nums):
        left = idx * 2 + 1
        right = idx * 2 + 2
        largest = idx
        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        
        if right < heap_size and nums[right] > nums[largest]:
            largest = right
        
        if largest != idx:
            nums[idx], nums[largest] = nums[largest], nums[idx]
            self.heapify(heap_size, largest, nums)

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
