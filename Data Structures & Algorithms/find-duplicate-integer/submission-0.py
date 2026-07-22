class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        # brute force -> O(n^2)
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1