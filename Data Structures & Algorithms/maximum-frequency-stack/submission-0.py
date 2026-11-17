from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cnt[val] += 1

    def pop(self) -> int:
        maxCnt = max(self.cnt.values())
        i = len(self.stack) - 1
        while self.cnt[self.stack[i]] != maxCnt:
            i -= 1
        self.cnt[self.stack[i]] -= 1
        return self.stack.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()