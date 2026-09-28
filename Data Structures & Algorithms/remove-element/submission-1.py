class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        0 1 3 0 4 2 2 2 and val == 2
                  L
                      R

        """
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return left