from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums: List[int], k: int) -> int:
            count = 0
            left = 0
            window = defaultdict(int)
            
            for right in range(len(nums)):
                window[nums[right]] += 1
                
                while len(window) > k:
                    window[nums[left]] -= 1
                    if window[nums[left]] == 0:
                        del window[nums[left]]
                    left += 1
                
                count += right - left + 1
                
            return count
        
        return atMostK(nums, k) - atMostK(nums, k - 1)