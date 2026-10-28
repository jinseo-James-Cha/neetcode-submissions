# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1 2 3 4 and n == 2
        0 1 2 3  

        remove 2nd node from the end only from the whole list
        I need to know the nth node one before

        1 -> 2 -> 4
            curr.next = curr.next.next
            curr removes curr.next

        1 2 3 4
          S
              F

        1 2
      S
          F
        """
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        move = n
        while move > 0:
            fast = fast.next
            move -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

        



