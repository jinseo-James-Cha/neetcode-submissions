class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        while right < n:
            nums[left] = nums[right]
            while right < n and nums[left] == nums[right]:
                right += 1
            
            left += 1
        return left