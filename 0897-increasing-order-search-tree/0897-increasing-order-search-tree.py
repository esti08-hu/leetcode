# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)

            self.prev.right = root
            root.left = None
            self.prev = root

            inorder(root.right)
        
        dummy = TreeNode(0)
        self.prev = dummy
        inorder(root)

        return dummy.right