# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        self.inOrder(root)
        return self.arrToBst(0, len(self.arr)-1)
    def inOrder(self,root:TreeNode) -> None:
        if not root: return 
        self.inOrder(root.left)
        self.arr.append(root)
        self.inOrder(root.right)
    def arrToBst(self, a:int,b:int) -> TreeNode:
        if a>b: return None
        m = (a+b)//2
        root = self.arr[m]
        root.left = self.arrToBst(a,m-1)
        root.right = self.arrToBst(m+1,b)
        return root