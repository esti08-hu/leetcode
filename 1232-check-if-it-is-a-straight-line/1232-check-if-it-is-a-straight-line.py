class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i-2]
            x2, y2 = coordinates[i-1]
            x3, y3 = coordinates[i]

            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
            
        
        return True