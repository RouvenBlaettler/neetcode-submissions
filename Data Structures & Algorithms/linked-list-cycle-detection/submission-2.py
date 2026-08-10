# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        s = set()
        tail = head
    
        while tail:
            seen.append(tail)
            s.add(tail)
            print(seen)
            print(s)
            if len(s) == len(seen):
                tail = tail.next
            else:
                return True


        return False