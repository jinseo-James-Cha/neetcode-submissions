# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



import heapq

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        min_heap = []
        for l in lists:
            if l:
                heapq.heappush(min_heap, HeapNode(l))
        
        res = ListNode()
        dummy = res
        while min_heap:
            min_heap_node = heapq.heappop(min_heap)
            min_node = min_heap_node.node

            dummy.next = min_node
            dummy = dummy.next

            if min_node.next:
                heapq.heappush(min_heap, HeapNode(min_node.next))
        return res.next


