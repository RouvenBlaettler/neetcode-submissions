# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        seen.add(1)

        while head:
            length1 = len(seen)
            seen.add(head)
            length2 = len(seen)
            if length1 == length2:
                return True
            head = head.next

        return False
            