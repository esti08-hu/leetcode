# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.max_path = max(self.max_path, root.val + left + right, root.val + left, root.val + right, root.val)
            if max(left, right) < 0:
                return root.val
                
            return root.val + max(left, right)
        
        dfs(root)
        return self.max_path
