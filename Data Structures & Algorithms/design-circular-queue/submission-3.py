"""
Doubly linked list
"""
class DoublyLinkedList:
    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.head = DoublyLinkedList(0, None, None)
        self.tail = DoublyLinkedList(0, None, self.head)
        self.head.next = self.tail

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        curr = DoublyLinkedList(value, self.tail, self.tail.prev)
        self.tail.prev.next = curr
        self.tail.prev = curr
        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.space += 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.prev.val
        
    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()