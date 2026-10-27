# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast and Slow pointers
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True

        return False
        
        
        # brute force
        # hashset -> tc:O(n) + sc:O(n)
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False