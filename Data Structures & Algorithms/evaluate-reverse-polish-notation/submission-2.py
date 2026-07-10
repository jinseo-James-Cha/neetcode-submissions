class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            #if token.isnumeric(): this cannot check negative numbers like -11
            if token not in "+-*/":
                num_stack.append(int(token))
            else:
                second_num = num_stack.pop()
                first_num = num_stack.pop()
                result_num = 0
                if token == "+":
                    result_num = first_num + second_num
                elif token == "-":
                    result_num = first_num - second_num
                elif token == "*":
                    result_num = first_num * second_num
                else:
                    result_num = int(first_num / second_num)
                num_stack.append(result_num)
        return num_stack[0]
