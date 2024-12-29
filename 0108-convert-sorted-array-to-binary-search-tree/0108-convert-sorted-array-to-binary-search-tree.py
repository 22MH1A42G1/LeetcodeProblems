# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        m = len(nums)//2
        n = TreeNode(nums[m])
        n.left = self.sortedArrayToBST(nums[:m])
        n.right = self.sortedArrayToBST(nums[m+1:])
        return n