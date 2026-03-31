# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, sRoot):
            if not root and not sRoot:
                return True
            if not root or not sRoot:
                return False
            if root.val != sRoot.val:
                return False
            if not check(root.left, sRoot.left) or not check(root.right, sRoot.right):
                return False
            
            return True

        def dfs(root):
            if not root:
                return False
            print(root.val)
            if root.val == subRoot.val:
                if check(root, subRoot):
                    return True
            
            if dfs(root.left) or dfs(root.right):
                return True
            
            return False
        
        return dfs(root)
