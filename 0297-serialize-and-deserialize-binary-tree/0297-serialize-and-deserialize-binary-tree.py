# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if root:
                arr.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                arr.append("#")
        arr = []
        dfs(root)
        return " ".join(arr)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            i=next(arr)
            if i=="#":
                return None
            root = TreeNode(int(i))
            root.left = dfs()
            root.right = dfs()
            return root
        arr = iter(data.split())
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))