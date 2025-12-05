class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        b 0 1 2
        t 1 2 3
        5 
        check(mid, time):
            trips = 0
            for i in range(len(time)):
                trips+=mid//time[i]
            
            if trips >= totalTrips:
                return True
            return False

            
        '''

        def check(mid):
            trips = 0
            for i in range(len(time)):
                trips+=mid//time[i]
            
            if trips >= totalTrips:
                return True
            return False
        
        l, r = 0, min(time) * totalTrips
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l