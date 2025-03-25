class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        best = -1

        while low <= high:
            mid = (low+high)//2
            #calculate the hour for the mid speed 
            cal_h = 0
            for pile in piles:
                cal_h+=math.ceil(pile/mid)
            

            if cal_h <= h:
                high = mid - 1
                best = mid

            else:
                low = mid + 1
        return best 


