class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        # sort
        # O(n log n) + O(1)
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                return nums[i]
        return -1

        # brute force - hashset
        # O(n) and O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1