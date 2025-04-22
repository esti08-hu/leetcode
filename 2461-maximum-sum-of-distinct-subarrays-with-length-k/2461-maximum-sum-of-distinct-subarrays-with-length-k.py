class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0
        curr_sum = 0
        window = {}  
        
        for i in range(k):
            if i < n:
                curr_sum += nums[i]
                window[nums[i]] = window.get(nums[i], 0) + 1
        
        if len(window) == k:
            max_sum = curr_sum
            
        for i in range(k, n):
            left_ele = nums[i - k]
            curr_sum -= left_ele
            window[left_ele] -= 1
            if window[left_ele] == 0:
                del window[left_ele]
                
            curr_sum += nums[i]
            window[nums[i]] = window.get(nums[i], 0) + 1
            
            if len(window) == k:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum