# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        # print(arr)
        i = 0
        j = len(arr)-1
        m = 0
        while i < j:
            m = max(m, arr[i]+arr[j])
            i+=1
            j-=1
        return m
