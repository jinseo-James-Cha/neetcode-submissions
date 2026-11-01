"""
if it doesn't matter FIFO rule, it would be hashset.
Hashset works with O(1) time for insert/update, and get operations.

However, this question requires to add new value even though
it is already full and remove the first element.

Therefore, I need something to do remove the first element O(1)
and add an element at the end O(1)
==> Doubly Linked List
"""
class DoublyLinkedList:
    def __init__(self, key, val, nxt, prev):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyLinkedList(0, 0, None, None)
        self.tail = DoublyLinkedList(0, 0, None, self.head)
        self.head.next = self.tail

        self.hashmap = {}

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        curr = self.hashmap[key]
        self.remove(curr)
        self.add(curr)
        return curr.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            del self.hashmap[key]
        
        new_node = DoublyLinkedList(key, value, None, None)
        self.hashmap[key] = new_node
        self.add(new_node)
        if len(self.hashmap) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.hashmap[lru.key]

    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev

        node.next = self.tail
        self.tail.prev = node

        
