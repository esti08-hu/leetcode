# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(s, node):
            if not node:
                return False
            
            curr_sum = s + node.val
            if not node.left and not node.right:
                return targetSum == curr_sum
            
            return dfs(curr_sum, node.left) or dfs(curr_sum, node.right)
        
        return dfs(0, root)