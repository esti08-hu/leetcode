class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        '''
        low = 1
        high = max(candies) = 8


        mid = 4

        count = 0

        for c in candies:
            curr = c
            while curr > k:
                curr-=mid
                count += 1
        
        return count >= k


        low = mid
        high = mid - 1

        return high
            
        1 + 8 = 9//2 = 4 + 8 = 12//2 = 5+4
        '''
        def can(mid):
            count = 0 

            for c in candies:
                curr = c
                count += c // mid

            return count >= k

        low = 1
        high = max(candies)
        ans = -1
        while low <= high:
            mid = (low+high) // 2

            if can(mid):
                low = mid + 1
                ans = mid 
            else:
                high = mid - 1
        
        return ans