# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = head

        if not newhead:
            return None

        if newhead.next:
            newhead = self.reverseList(newhead.next)
            head.next.next = head
        head.next = None
        return newhead
