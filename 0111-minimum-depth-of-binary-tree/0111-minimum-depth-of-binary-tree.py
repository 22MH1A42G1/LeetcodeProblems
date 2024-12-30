# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root, 1)])
        while q:
            n,d = q.popleft()
            if not n.left and not n.right: return d
            if n.left: q.append((n.left,d+1))
            if n.right: q.append((n.right,d+1))