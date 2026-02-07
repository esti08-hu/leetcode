# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def bin_int(b):
            total = 0
            b = b[::-1]
            for i in range(len(b)):
                if b[i] == "1":
                    total += 2**i
            return total

        self.res = 0

        def preorder(root, curr):
            if not root:
                return 

            if not root.left and not root.right:
                curr_ = curr + str(root.val)

                self.res += bin_int(list(curr_))
                return 

            preorder(root.left, curr+str(root.val))
            preorder(root.right, curr+str(root.val))

        preorder(root, "")

        return self.res