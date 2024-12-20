# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root) -> TreeNode:
        self.__traverse_DFS(root.left, root.right, 0)
        return root

    def __traverse_DFS(self, left_child, right_child, level):
        if left_child is None or right_child is None:
            return
        # If the current level is odd, swap the values of the children.
        if level % 2 == 0:
            temp = left_child.val
            left_child.val = right_child.val
            right_child.val = temp

        self.__traverse_DFS(left_child.left, right_child.right, level + 1)
        self.__traverse_DFS(left_child.right, right_child.left, level + 1)
        
        