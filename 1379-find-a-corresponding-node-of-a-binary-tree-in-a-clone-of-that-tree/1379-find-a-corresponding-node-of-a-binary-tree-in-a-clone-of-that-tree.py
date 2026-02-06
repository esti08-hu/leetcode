# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def preorder(root):
            if not root:
                return 
            if root.val == target.val:
                return root
            
            left = preorder(root.left)
            right = preorder(root.right)

            return left if left else right
        
        return preorder(cloned)