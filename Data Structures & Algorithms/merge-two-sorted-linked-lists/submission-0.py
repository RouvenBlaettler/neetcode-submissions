# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = list1, list2

        dummy = ListNode()
        tail = dummy

        while second and first:
            if first.val < second.val:
                tail.next = first
                first = first.next

            else:
                tail.next = second
                second = second.next
            tail = tail.next

        while first:
            tail.next = first
            first = first.next
            tail = tail.next
        
        while second:
            tail.next = second
            second = second.next
            tail = tail.next

        return dummy.next