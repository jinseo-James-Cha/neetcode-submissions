class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        two pointers
        move smaller part into inward
        """
        left = 0
        right = len(heights) - 1
        maximum_amount = 0

        while left < right:
            curr_height = min(heights[left], heights[right])
            curr_width = right - left
            maximum_amount = max(maximum_amount, curr_height * curr_width)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1
        return maximum_amount