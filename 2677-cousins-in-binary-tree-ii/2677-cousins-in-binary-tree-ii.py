# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return
            total_sum = 0
            for node in arr:
                if not node:
                    continue
                if node.left:
                    total_sum += node.left.val
                if node.right:
                    total_sum += node.right.val
            childArr = []
            for node in arr:
                curSum = 0
                if node.left:
                    curSum += node.left.val
                if node.right:
                    curSum += node.right.val
                if node.left:
                    node.left.val = total_sum - curSum
                    childArr.append(node.left)
                if node.right:
                    node.right.val = total_sum - curSum
                    childArr.append(node.right)
            dfs(childArr)

        root.val = 0
        dfs([root])
        return root