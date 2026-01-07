# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans, total=-inf, 0
        def dfs(root):
            nonlocal ans, total
            if not root: return 0
            Sum=root.val+dfs(root.left)+dfs(root.right)
            ans=max(ans, (total-Sum)*Sum)
            return Sum
        total=dfs(root)
        dfs(root)
        return ans%(10**9+7)