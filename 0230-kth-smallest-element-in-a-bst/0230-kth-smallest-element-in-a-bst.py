# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = k
        self.res = -1
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            self.n-=1
            if not self.n:
                self.res = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return self.res
