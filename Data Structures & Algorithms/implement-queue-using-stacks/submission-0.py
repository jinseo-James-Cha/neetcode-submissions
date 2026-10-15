"""
First In First Out -> queue -> using two stacks.

1 -> 2 -> 3 -> 4 -> 5


"""

class MyQueue:

    def __init__(self):
        self.s1 = [] # 1 2 3

    def push(self, x: int) -> None:
        self.s1.append(x) # 1 2 3 4
    
    def pop(self) -> int:
        stack = []
        for num in reversed(self.s1):
            stack.append(num) # 4 3 2 1
        
        poped = stack.pop()
        self.s1 = stack[::-1]
        return poped
        
    def peek(self) -> int:
        return self.s1[0]
        
    def empty(self) -> bool:
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()