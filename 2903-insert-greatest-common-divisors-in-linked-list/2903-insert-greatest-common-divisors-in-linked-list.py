# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            gcd_val = math.gcd(curr.val, curr.next.val)
            gcd_node = ListNode(gcd_val)  # Create new node with the GCD
            gcd_node.next = curr.next     # Point new node to the next node
            curr.next = gcd_node          # Insert GCD node after current
            curr = gcd_node.next          # Move to the next pair
        return head