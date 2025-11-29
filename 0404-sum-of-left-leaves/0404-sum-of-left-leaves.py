# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return
            
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.res