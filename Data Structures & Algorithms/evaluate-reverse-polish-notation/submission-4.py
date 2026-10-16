class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                first_prev = stack.pop()
                second_prev = stack.pop()
                
                if token == "+":
                    stack.append(second_prev + first_prev)
                elif token == "-":
                    stack.append(second_prev - first_prev)
                elif token == "*":
                    stack.append(second_prev * first_prev)
                else:
                    stack.append(int(second_prev / first_prev))
            else:
                stack.append(int(token))

        return stack[0]