"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True, None, None, None, None)
        mid = n // 2
        topLeft = self.construct([row[:mid] for row in grid[:mid]])
        topRight = self.construct([row[mid:] for row in grid[:mid]])
        bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
        bottomRight = self.construct([row[mid:] for row in grid[mid:]])
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            return Node(topLeft.val, True, None, None, None, None)
        return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
