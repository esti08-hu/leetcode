# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_map = set()

        def inorder(root):
            if not root:
                return 
            if k - root.val in hash_map:
                return True
            else:
                hash_map.add(root.val)
            if inorder(root.left) or inorder(root.right):
                return True
            
        if inorder(root):
            return True
        else:
            return False
