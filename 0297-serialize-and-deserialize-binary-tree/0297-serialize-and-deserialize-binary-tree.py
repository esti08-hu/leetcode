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
        res = []
        
        q = collections.deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    res.append("N")
                else:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        
        return ",".join(map(str, res))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode

        arr = data.split(",")
        i = 0
        q = [1]
        while q:
            for _ range(len(q))
                if node:
                node = TreeNode(int(arr[i]))
                if arr[(i*2)+1] not equal to N
                    node.left = TreeNode(int(arr[(i*2)+1]))
                else:
                    node.left = None
                node.right = TreeNode(int(arr[(i*2)+2]))
        """

        vals = data.split(",")

        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i+=1

            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i+=1

            
        return root
            




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))