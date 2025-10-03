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

            nl = 0
            nr = 0
            if node.left:
                nl = max(nl, dfs(node.left.left) + dfs(node.left.right))

            if node.right:
                nr = max(nr, dfs(node.right.right) + dfs(node.right.left))

            res = max(node.val + nl+ nr, dfs(node.left) + dfs(node.right))

            return res
        return dfs(root)
