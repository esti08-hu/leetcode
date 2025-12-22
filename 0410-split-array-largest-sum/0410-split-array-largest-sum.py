class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_cap):
            cuts = 1
            curr_sum = 0

            for num in nums:
                curr_sum += num
                if curr_sum > max_cap:
                    cuts += 1
                    curr_sum = num
            
            return cuts <= k
        
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) >> 1

            if can_split(mid):
                high = mid
            else:
                low = mid + 1
            
        return low