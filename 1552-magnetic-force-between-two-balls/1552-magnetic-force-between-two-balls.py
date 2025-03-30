class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(force):
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i]-last_pos >= force:
                    count+=1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1]-position[0]
        res = 0

        while left <= right:

            mid = (left+right)//2

            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1 
        
        return res