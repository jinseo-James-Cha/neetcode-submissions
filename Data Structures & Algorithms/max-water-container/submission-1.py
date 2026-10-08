class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        two pointers
        move smaller part into inward
        """
        n = len(heights)
        left = 0
        right = n - 1

        most_water = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            most_water = max(most_water, width * height)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return most_water