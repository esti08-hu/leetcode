# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return 
            if not root.left and not root.right:
                return root

            right = dfs(root.right)
            left = dfs(root.left)

            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
            
            return right if right else left
        
        dfs(root)