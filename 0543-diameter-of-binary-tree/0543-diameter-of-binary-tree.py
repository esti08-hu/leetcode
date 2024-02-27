class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            self.diameter = max(self.diameter, left_height + right_height)
            
            return max(left_height, right_height) + 1
        
        height(root)
        return self.diameter