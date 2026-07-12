class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        7 - - - - - - -
        1 -
        7 - - - - - - -
        2 - -
        2 - -
        4 - - - -

        7 -> current max
        1 -> min(7, 1) * 1 - 0 + 1 -> 2
        7 -> min(7, 1) * 2 - 0 + 1 -> 3
        """
        # Monotonic stack

        n = len(heights)
        stack = []
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n
        for i in range(n -1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        maxRec = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxRec = max(maxRec, heights[i] * (rightMost[i] - leftMost[i] + 1))

        return maxRec


