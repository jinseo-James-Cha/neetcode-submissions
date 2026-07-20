# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1 2 3 4
        0 1 2 3

        remove 2th node from the end

        1 2 3 4
          S N F
        
        1 2   4
          S ->F

        """
        dummy = ListNode()
        dummy.next = head
        
        slow = dummy
        fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next



