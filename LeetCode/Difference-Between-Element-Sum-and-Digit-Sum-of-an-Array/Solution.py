1class Solution:
2    def differenceOfSum(self, nums: list[int]) -> int:
3        e_sum = sum(nums)
4
5        d_sum = 0
6
7        for num in nums:
8            curr = str(num)
9            for c in curr:
10                d_sum += int(c)
11        
12        return abs(e_sum - d_sum)