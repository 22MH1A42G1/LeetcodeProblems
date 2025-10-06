# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l2 is None: return l1
        elif l1 is None: return l2
        d=ListNode()
        c=d
        while l1 and l2:
            if l1.val <= l2.val:
                c.next=l1
                l1=l1.next
            else:
                c.next=l2
                l2=l2.next
            c=c.next
        if l1: c.next=l1
        else: c.next=l2
        return d.next
        # if l1.val<=l2.val:
        #     l1.next=self.mergeTwoLists(l1.next,l2)
        #     return l1
        # else:
        #     l2.next=self.mergeTwoLists(l1,l2.next)
        #     return l2