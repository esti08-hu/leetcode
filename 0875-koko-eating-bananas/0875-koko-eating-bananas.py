class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) > h:
        #     return 
        '''
        mn = 1
        mx = max(piles)

        check(mid)
            curr_hour = 0
            for i in range(len(piles))
                curr_hour += math.ceil(piles[i]/mid)
                if curr_hour > h:
                    return False
            
            return True
            
        '''
        def check(mid):
            curr_hour = 0
            for i in range(len(piles)):
                curr_hour += math.ceil(piles[i]/mid)
                if curr_hour > h:
                    return False
            return True

        mn, mx = 1, max(piles)

        while mn <= mx:
            mid = (mn + mx) // 2
            if check(mid):
                mx = mid - 1
            else:
                mn = mid + 1
        
        return mn
