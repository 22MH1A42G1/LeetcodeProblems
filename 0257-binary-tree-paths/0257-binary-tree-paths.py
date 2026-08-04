# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        r = []
        if not root: return r
        s = [(root,str(root.val))]
        while s:
            n, p = s.pop()
            if not n.left and not n.right:
                r.append(p)
            if n.right:
                s.append((n.right,p+'->'+str(n.right.val)))
            if n.left:
                s.append((n.left,p+'->'+str(n.left.val)))
        return r