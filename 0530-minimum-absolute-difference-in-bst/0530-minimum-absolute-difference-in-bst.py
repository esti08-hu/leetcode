# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def dfs(root, node, curr_res):
            if not node:
                return curr_res
            
            curr_res = min(curr_res, abs(root.val - node.val))
            left = min(curr_res, dfs(node, node.left, curr_res))
            right = min(curr_res, dfs(node, node.right, curr_res))

            return min(left, right)
        
        left = dfs(root, root.left, float("inf"))
        right = dfs(root, root.right, float("inf"))

        return min(left, right)