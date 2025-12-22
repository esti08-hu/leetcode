# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(root):
            if not root:
                return 0
            
            skip = dfs(root.left) + dfs(root.right)
            rob = root.val
            if root.left:
                rob += (dfs(root.left.left) + dfs(root.left.right))
            if root.right:
                rob += (dfs(root.right.left) + dfs(root.right.right))

            return max(skip, rob)
        
        return dfs(root)