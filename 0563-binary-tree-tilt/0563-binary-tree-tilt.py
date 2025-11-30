# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        '''
                    15                18      =  3
        21 (7 + 1 + 1 + 3 + 3) - (14 + 2 + 2) => 
        '''
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.res += abs(left - right)
            
            return left + right + root.val

        dfs(root)
        return self.res