1class Solution:
2    def differenceOfSum(self, nums: list[int]) -> int:
3        e_sum = sum(nums)
4
5        d_sum = 0
6
7        for num in nums:
8            curr = num
9            while curr > 0:
10                d_sum += (curr % 10)
11                curr //= 10
12        
13        return abs(e_sum - d_sum)