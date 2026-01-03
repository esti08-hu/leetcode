class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_x, max_y = 0, 0

        for x, y in points:
            max_x = max(x, max_x)
            max_y = max(y, max_y)
        
        return max_x * max_y / 2