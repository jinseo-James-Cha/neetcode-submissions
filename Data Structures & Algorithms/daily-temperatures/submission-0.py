class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                day = stack.pop()
                res[day] = i - day
            stack.append(i)
        
        return res