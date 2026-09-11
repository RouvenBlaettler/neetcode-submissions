# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur, prev = head, None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        dummy = ListNode()
        dummy.next = prev
        head_ptr = dummy

        for _ in range(n-1):
            dummy = dummy.next

        dummy.next = dummy.next.next

        cur, prev = head_ptr.next, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

        

        
