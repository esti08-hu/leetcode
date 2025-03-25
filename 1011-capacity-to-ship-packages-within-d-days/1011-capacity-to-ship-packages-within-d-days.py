class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        def check(cap):
            w_sum = 0
            D = 0
            for w in weights:
                w_sum += w
                if w_sum == cap:
                    D+=1
                    w_sum = 0
                elif w_sum > cap:
                    D+=1
                    w_sum=0
                    w_sum += w
            if w_sum > 0:
                D+=1
            return D <= days



        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                high = mid-1
            else:
                low = mid + 1
        
        return low 