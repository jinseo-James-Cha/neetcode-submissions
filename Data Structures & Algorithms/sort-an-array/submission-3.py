import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Heap sort - avg O(n log n) -> worst O(n log n)
        self.heap_sort(nums)
        return nums

        # Merge sort - avg O(n log n) -> worst O(n log n)
        # merged_sort_nums = self.merge_sort(nums)
        # return merged_sort_nums

        # Quick sort - avg O(n log n) -> worst O(n^2)
        # self.quick_sort(nums, 0, len(nums) - 1)
        # return nums
    
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
    


    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left_arr = self.merge_sort(nums[:mid])
        right_arr = self.merge_sort(nums[mid:])
        return self.merge(left_arr, right_arr)
    
    def merge(self, left_arr, right_arr):
        res = []
        i = j = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                res.append(left_arr[i])
                i += 1
            else:
                res.append(right_arr[j])
                j += 1
        res.extend(left_arr[i:])
        res.extend(right_arr[j:])
        return res

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