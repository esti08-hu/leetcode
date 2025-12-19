class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        low = days equal to len weights
        high = their is only one day

        low = max(weights)
        high = sum(weights)
        mid = (low + high) >> 1
        can_ship(max_cap):

        curr_sum = 0
        count = 1

        for weight in weights:
            curr_sum += weight

            if curr_sum > max_cap:
                count += 1
                curr_sum = weight
        return count <= days

        while low < right:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid
            else:
                left = mid + 1
        return low 

        '''
        def can_ship(max_cap):
            curr_sum = 0
            count = 1
            
            for weight in weights:
                curr_sum += weight

                if curr_sum > max_cap:
                    count += 1
                    curr_sum = weight
                
            return count <= days

        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) >> 1

            if can_ship(mid):
                high = mid
            else:
                low = mid + 1
        
        return low