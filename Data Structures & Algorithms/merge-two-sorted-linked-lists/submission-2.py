# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        - merge two sorted linked list
        - keep going even though one linked list is ended
        """

        merged_list = ListNode()
        dummy = merged_list

        while list1 or list2:
            curr_var_list1 = list1.val if list1 else float('inf')
            curr_var_list2 = list2.val if list2 else float('inf')

            if curr_var_list1 > curr_var_list2:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        
        return merged_list.next