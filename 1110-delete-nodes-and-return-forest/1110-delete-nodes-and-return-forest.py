# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root, to_delete):
        delete = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in delete:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None

            return node

        root = dfs(root)

        if root:
            forest.append(root)

        return forest