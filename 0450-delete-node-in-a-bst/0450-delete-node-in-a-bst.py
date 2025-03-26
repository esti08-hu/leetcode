# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getMin(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr

        def remove(node, key):
            if not node:
                return None

            if node.val > key:
                node.left = remove(node.left, key)
            elif node.val < key:
                node.right = remove(node.right, key)
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    successor = getMin(node.right)
                    node.val = successor.val  

                    node.right = remove(node.right, successor.val) 

            return node

        return remove(root, key)