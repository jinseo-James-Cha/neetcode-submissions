class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        distinct integers, sorted in ascending order
        find target's index or return -1
        """

        # brute force
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1