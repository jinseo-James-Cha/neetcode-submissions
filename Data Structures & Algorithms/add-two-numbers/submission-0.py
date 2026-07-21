# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        not gaurantee they have the same length?
        if not, assump 0
        """

        res = ListNode()
        dummy = res
        carry = 0
        while l1 or l2:
            l1_num = 0
            if l1:
                l1_num = l1.val
                l1 = l1.next

            l2_num = 0
            if l2:
                l2_num = l2.val
                l2 = l2.next

            curr_total = l1_num + l2_num + carry
            dummy.next = ListNode(curr_total % 10)
            dummy = dummy.next
            carry = curr_total // 10
        
        if carry:
            dummy.next = ListNode(carry)
        
        return res.next