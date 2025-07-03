# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(n,r):
            if not n: return
            fun(n.left,r)
            fun(n.right,r)
            r.append(n.val)
        r=[]
        fun(root,r)
        return r