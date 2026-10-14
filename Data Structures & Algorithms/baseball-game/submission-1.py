class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        start with empty record
        + = record a sum with two previous
        D = record a double of the previous
        C = remove a prev record
        """
        stack = []
        for ch in operations:
            if ch == "+":
                prev = stack[-1]
                prev_prev = stack[-2]
                stack.append(prev + prev_prev)
            elif ch == "D":
                stack.append(2 * stack[-1])
            elif ch == "C":
                stack.pop()
            else:
                stack.append(int(ch))
        return sum(stack)