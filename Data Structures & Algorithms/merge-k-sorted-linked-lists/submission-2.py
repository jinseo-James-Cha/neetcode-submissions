# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    # heapq
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode()
        curr = res
        minHeap = []

        for l in lists:
            if l:
                heapq.heappush(minHeap, HeapNode(l))
        
        while minHeap:
            min_heap_node = heapq.heappop(minHeap)
            curr.next = min_heap_node.node
            curr = curr.next

            if min_heap_node.node.next:
                heapq.heappush(minHeap, HeapNode(min_heap_node.node.next))
        return res.next



    # separate merge two lists
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        return lists[-1]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
        

        # one pass
        res = ListNode()
        dummy = res

        while True:
            min_node = -1
            for i, node in enumerate(lists):
                if not node:
                    continue

                if min_node == -1 or node.val < lists[min_node].val:
                    min_node = i
            
            if min_node == -1:
                break

            dummy.next = lists[min_node]
            lists[min_node] = lists[min_node].next
            dummy = dummy.next
        
        return res.next