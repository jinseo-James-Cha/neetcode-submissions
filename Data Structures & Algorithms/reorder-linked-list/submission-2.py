# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        2 4 6 8
        ->   <-

        2 -> 4
        8 -> 6
        find middle and disconnect to middle which is left
        and then reverse mid to end which is the right
        
        merge two linked list then

        2 8 4 6
        L R L R

        2 4 6 8
          S
              F
        """
        if not head or not head.next:
            return
            
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev


        # find middle with Fast and Slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # make disconnection with the second half
        right = slow.next
        slow.next = None
        right = reverse(right)

        left = head
        while right:
            left_temp = left.next
            right_temp = right.next

            left.next = right
            right.next = left_temp

            left = left_temp
            right = right_temp


        