class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        [[10,16],[2,8],[1,6],[7,12]]

        [1,6][2,8][7,12][10,16]
        '''

        points.sort(key=lambda x:x[1])
        
        arrows = 1
        last_end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > last_end:
                arrows += 1
                last_end = points[i][1]
        
        return arrows


