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
                return float("-inf")
            
            left = dfs(root.left)
            right = dfs(root.right)
            if root.left or root.right:
                self.max_path = max(self.max_path, left, left + root.val, right + root.val, right, root.val, left + right + root.val)
            if not root.left and not root.right:
                self.max_path = max(self.max_path, root.val)
            curr_max = max(root.val, root.val+left, root.val+right)
            if curr_max < 0:
                return float("-inf")
            else:
                return curr_max
        dfs(root)
        return self.max_path