class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        # sorting -> O(n log n)
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:
            if prev == num:
                return num
            prev = num
        return -1

        # brute force -> O(n^2)
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1