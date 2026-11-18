# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next

        l1 = l[:len(l)//2]
        l2 = l[len(l)//2:][::-1]
        new_l = []
        for i in range(len(l1)):
            new_l.append(l1[i])
            new_l.append(l2[i])
        if len(l1) < len(l2):
            new_l.append(l2[-1])
        

        for i in range(len(new_l) - 1):
            new_l[i].next = new_l[i + 1]
        new_l[-1].next = None   


        

        