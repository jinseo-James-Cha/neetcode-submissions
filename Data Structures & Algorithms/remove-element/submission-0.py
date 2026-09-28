class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        3 2 2 3 and val == 3
        X O O X
        L
          R
        2 3 2 3
          L
            R
        2 2 3 3
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