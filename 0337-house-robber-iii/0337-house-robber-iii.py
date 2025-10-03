# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node:
                return 0
            
            take = node.val

            if node.left:
                take+= dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                take+= dfs(node.right.left) + dfs(node.right.right)
            
            not_take = dfs(node.right) + dfs(node.left)

            return max(take, not_take)


        return dfs(root)
