class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(nums, k, max_sum):
            current_sum = 0
            subarrays = 1 

            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k: 
                        
                        return False
                else:
                    current_sum += num
            return True

        left, right = max(nums), sum(nums)
        res = right

        while left <= right:
            mid = (left + right) // 2
            if canSplit(nums, k, mid):
                res = mid 
                
                right = mid - 1 
                
            else:
                left = mid + 1 
                
        return res