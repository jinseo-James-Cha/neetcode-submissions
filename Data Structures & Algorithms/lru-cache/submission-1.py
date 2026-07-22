class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    """
    Run in O(1) average Time complexity
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyLinkedList(-1,-1)
        self.tail = DoublyLinkedList(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def remove(self, removing_node):
        removing_node.prev.next = removing_node.next
        removing_node.next.prev = removing_node.prev

    def add(self, adding_node):
        prev_tail = self.tail.prev

        prev_tail.next = adding_node
        adding_node.prev = prev_tail

        self.tail.prev = adding_node
        adding_node.next = self.tail


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # if found -> cuz update queue recently used
        # remove prev position and add to tail
        found_node = self.cache[key]
        self.remove(found_node)
        self.add(found_node)
        return found_node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            curr_node = self.cache[key]
            curr_node.val = value
            self.remove(curr_node)
            self.add(curr_node)
            return
        
        new_node = DoublyLinkedList(key, value)
        self.add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            least_recent_node = self.head.next
            self.remove(least_recent_node)
            del self.cache[least_recent_node.key]