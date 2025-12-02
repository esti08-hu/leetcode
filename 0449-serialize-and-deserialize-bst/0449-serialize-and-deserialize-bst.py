# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        self.tree = ""
        if not root:
            return self.tree

        def preorder(root):
            if not root:
                return

            if not self.tree:
                self.tree+=str(root.val)
            else:
                self.tree+=(","+str(root.val))
            
            preorder(root.left)
            preorder(root.right)
            
            return self.tree

        return preorder(root)
            
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split(",")
        
        root = TreeNode(data[0])
        def dfs(root, i):
            if root == "N" or i >= len(data):
                return 

            if i*2+1 < len(data):
                root.left = TreeNode(data[i*2+1])
                dfs(root.left, i*2+1)
            if i*2+2 < len(data):
                root.right = TreeNode(data[i*2+2])
                dfs(root.right, i*2+2)
        
        dfs(root, 0)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return an