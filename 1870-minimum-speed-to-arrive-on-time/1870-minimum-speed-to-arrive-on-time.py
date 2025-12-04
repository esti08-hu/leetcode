class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        '''
        0 1 2 
        1 3 2 
        mx = 3
        mi = 0
        1 + 3 + 2 => 6
        mid = 1

        hour = 6
dist = [1,3,2,4], hour = 6

mx = 4
mi = 0
mid = 1
1 + 1 + 0.7 = 2.7 == 2.7 =>  
ans = -1
if i == len(nums) - 1:
    curr_hour += dist[i]/mid
else:
    curr_hour += math.ceil(dist[i]/mid)

if curr_hour == hour => return mid
if curr_hour > hour  =>  mi = mid + 1
if curr_hour < hour => ans = mid; mx = mid

return ans

        '''
        if hour <= len(dist) - 1:
            return -1
        mx = 10**7
        mn = 1

        ans = -1
        while mn < mx:
            mid = (mx + mn)//2
            curr_hour = 0
            for i in range(len(dist)):
                if i == len(dist)-1:
                    curr_hour+=dist[i]/mid
                else:
                    curr_hour+=math.ceil(dist[i]/mid)

            if curr_hour > hour:
                mn = mid + 1
            else:
                mx = mid

        return mn
