# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        1 -> 2 -> 3 -> 4 -> 5
        L         R

        reverse 1 2 3 => 3 2 1 and then connect the rest
        3 2 1 -> 4 -> 5

        1 2 3 4 5
          L   R

        Right - Left + 1 = how many nodes need to reverse

        I need three part
        before left node, right node and after right node

        1 2 3 4 5
       L
       R
        """
        if left == right:
            return head
        
        def reverse(head, size):
            prev = None
            curr = head
            while curr and size > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                size -= 1

            return prev

        size = right - left + 1
        
        dummy = ListNode()
        dummy.next = head
        left_node = dummy
        right_node = dummy

        # Find node before left
        for _ in range(left - 1):
            left_node = left_node.next

        # Find right node
        for _ in range(right):
            right_node = right_node.next

        first_node = left_node.next
        after_right = right_node.next

        reversed_node = reverse(first_node, size)

        left_node.next = reversed_node
        first_node.next = after_right

        return dummy.next



        