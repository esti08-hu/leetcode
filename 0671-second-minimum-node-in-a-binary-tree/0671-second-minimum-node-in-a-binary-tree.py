# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.second_min = float('inf')
        first_min = root.val
        
        def dfs(node):
            if not node:
                return
                
            if first_min < node.val < self.second_min:
                self.second_min = node.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.second_min if self.second_min != float('inf') else -1