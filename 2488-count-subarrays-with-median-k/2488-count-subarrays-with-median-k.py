from collections import defaultdict
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        p2_counter = defaultdict(int)
        p2 = 0
        idx = nums.index(k)
        
        for i in range(idx+1, len(nums)):
            if nums[i] < k:
                p2 -= 1
            elif nums[i] > k:
                p2 += 1
            p2_counter[p2] += 1
        p2_counter[0] += 1

        p1 = 0
        res = 0

        for i in range(idx, -1, -1):
            if nums[i] < k:
                p1 -= 1
            elif nums[i] > k:
                p1 += 1
            res += p2_counter[-p1]
            res+=p2_counter[1-p1]

        return res