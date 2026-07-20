# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        reorder
        beginning end beginning+1 end-1 ... to half

        0 1 2 3
        0 3 1 2  => 2 times

        0 1 2 3 4
        0 4 1 3 2 => 2 times + beginning one

        idea
        move a pointer to the end
        -> length count
        -> make reverse linked list length //2 
        and head -> revered linked -> head.next -> ...?

        """
        # find middle -> reverse second half -> merge
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2








