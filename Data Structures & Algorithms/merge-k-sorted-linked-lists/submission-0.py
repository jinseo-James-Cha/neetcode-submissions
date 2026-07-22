# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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