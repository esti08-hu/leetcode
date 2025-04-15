# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        dq = deque([root])
        value = root.val

        while dq:
            node = dq.popleft()

            if value != node.val:
                return False
            
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        return True