class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        min_index = -1
        
        for i, (px, py) in enumerate(points):
            # Check if point is valid (shares x or y)
            if px == x or py == y:
                # Calculate distance
                dist = abs(x - px) + abs(y - py)
                
                # Update if we found a smaller distance
                if dist < min_dist:
                    min_dist = dist
                    min_index = i
                    
        return min_index