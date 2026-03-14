class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_cnt = Counter(nums)
        ans = 0
        for k, v in nums_cnt.items():
            if v == 1:
                ans += k
        
        return ans


