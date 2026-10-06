class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

        n = len(nums)
        left = 0
        right = 0
        while right < n:
            nums[left] = nums[right]
            while right < n and nums[left] == nums[right]:
                right += 1
            
            left += 1
        return left