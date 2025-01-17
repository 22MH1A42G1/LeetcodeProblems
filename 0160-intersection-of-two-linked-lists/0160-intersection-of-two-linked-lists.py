# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        d1,d2=headA,headB
        while d1!=d2:
            d1=d1.next if d1 else headB
            d2=d2.next if d2 else headA
        return d1