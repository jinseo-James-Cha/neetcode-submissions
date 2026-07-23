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
        # iteration
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            prev = kth.next #
            curr = groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            temp = groupPrev.next
            groupPrev.next = kth 
            groupPrev = temp 

        return dummy.next






        # iteration
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next # 4 

            prev = kth.next # 4
            curr = groupPrev.next # 1
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next # 1
            groupPrev.next = kth # 1->4
            groupPrev = temp # 1
        return dummy.next



        # recursion
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