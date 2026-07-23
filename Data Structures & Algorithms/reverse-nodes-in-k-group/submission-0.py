# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1 2 3 4 5 6 None, k = 3

        3 2 1 6 5 4 None

        if a group has less than k, it doesn't reverse

        slow and fast pointers
        slow meets fast then reverse, otherwise do nothing
        """
        # def reverse_list_node(begin, end):
        #     prev = ListNode(end)
        #     while begin != end:
        #         temp = begin.next
        #         begin.next = prev
        #         prev = begin
        #         begin = temp
            
        #     prev.next = end
        #     return prev

        curr = head
        curr_group = 0
        while curr and curr_group < k:
            curr = curr.next
            curr_group += 1
        
        if curr_group == k:
            curr = self.reverseKGroup(curr, k)
            while curr_group > 0:
                temp = head.next
                head.next = curr
                curr = head
                head = temp
                curr_group -= 1
            head = curr
        return head