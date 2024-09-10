"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, n: 'Node') -> List[int]:
        return n and sum(map(self.postorder,n.children),[])+[n.val] or []
