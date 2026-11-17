class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        curr = ""
        k = 0
        for c in s:
            if c.isnumeric():
                k = k * 10 + int(c)
            elif c == "[":
                string_stack.append(curr)
                count_stack.append(k)
                curr = ""
                k = 0
            elif c == "]":
                temp = curr
                curr = string_stack.pop()
                count = count_stack.pop()
                curr += temp * count
            else:
                curr += c
        return curr


        # one stack
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        
        return "".join(stack)
            
