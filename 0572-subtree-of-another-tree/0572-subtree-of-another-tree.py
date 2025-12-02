# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        root, subRoot, flag,
        flag = True => if 
        '''
        def check(node, subNode):
            if not node and not subNode:
                return True

            if not node or not subNode:
                return False

            if node.val != subNode.val:
                return False
            
            left = check(node.left, subNode.left)
            right = check(node.right, subNode.right)
            return left and right

        self.res = False
        def inorder(root):
            if not root:
                return 
            if not self.res and root.val == subRoot.val:
                self.res = (check(root, subRoot))
            
            inorder(root.left)
            inorder(root.right)
            return self.res

        return inorder(root)
