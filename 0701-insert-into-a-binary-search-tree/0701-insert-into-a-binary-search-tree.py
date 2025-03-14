# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            while node:
                if not node.right and not node.left:
                    return node

                if node.val > val:
                    if node.left:
                        node = dfs(node.left)
                    else:
                        return node

                elif node.val < val:
                    if node.right:
                        node = dfs(node.right)
                    else:
                        return node
                
        node = dfs(root)
        new_node = TreeNode(val)
        if not node:
            return new_node
            
        if val > node.val:
            node.right = new_node
        else:
            node.left = new_node
        
        return root