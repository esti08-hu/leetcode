class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        p = points[0]
        count =  1
        for i in range(len(points)):
            if p[1] < points[i][0]:
                p = points[i]
                count+=1
                
        return count