class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        0 1 2 3 4
        5,4,3,2,1

        1,2,3,4,7
        last_p = position[0]
        count = 1
        for p in position:
            gap = p - last_p
            if gap >= mid:
                last_p = p
                count += 1

        return count >= m

        low = 1
        high = max(position)
        '''
        position.sort()

        def can(mid):
            last_p = position[0]
            count = 1
            for p in position:
                gap = p - last_p
                if gap >= mid:
                    last_p = p
                    count += 1
            
            return count >= m
        
        low, high = 1, max(position)
        ans = -1
        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
