class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_capacity):
            cuts = 1
            current_sum = 0

            for num in nums:
                current_sum += num
                
                if current_sum > max_capacity:
                    cuts+=1
                    current_sum = num
            
            return cuts <= k
        

        low = max(nums)
        high = sum(nums)

        while low < high:
            mid  = (low + high) // 2

            if can_split(mid):
                high = mid
            else:
                low = mid + 1
        
        return low