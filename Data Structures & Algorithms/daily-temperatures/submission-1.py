class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        how many days need to see warmer temp
        """

        n = len(temperatures)
        res = [0] * n # 1 0 1
        stack = [] # index stack 1 1

        for i in range(n):
            # find less temp than today
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day

            # add today
            stack.append(i)
        return res