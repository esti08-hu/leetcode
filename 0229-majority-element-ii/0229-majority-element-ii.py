from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        nums_count = Counter(nums)
        for key, val in nums_count.items():
            if float(val) > len(nums)/3:
                res.append(key)
        
        return res
