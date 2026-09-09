# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        sec = prev
        first = head

        while sec:
            tmp1 = first.next
            tmp2 = sec.next
            first.next = sec
            sec.next = tmp1
            first = tmp1
            sec = tmp2

        