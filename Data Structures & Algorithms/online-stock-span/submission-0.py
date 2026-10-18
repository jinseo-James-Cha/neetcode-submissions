"""
return span of that stock's price for the current day.

span == stock's price is the maximum number of consecutive days starting from current to prev backward
        less or equal to the price

for example
7 2 1 2 2
        Today
  4 3 2 1 ->

7 34 1 2 Today
         8
"""

class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1
        curr = self.stack[:]
        while curr and curr[-1] <= price:
            span += 1
            curr.pop()
        
        self.stack.append(price)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)