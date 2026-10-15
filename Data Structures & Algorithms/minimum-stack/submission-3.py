class MinStack:

    def __init__(self):
        self.stack = [] # 1 2
        self.min_stack = [] # 1 1
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]


    # this is O(n) -> TLE
    # def getMin(self) -> int:
    #     min_val = float('inf')
    #     for num in self.stack:
    #         min_val = min(min_val, num)
    #     return min_val
        