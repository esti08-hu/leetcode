1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        min_sum = float("inf")
4        for num in nums:
5            curr = 0
6            while num > 0:
7                rem = num % 10
8                curr += rem
9                num = num // 10
10            min_sum = min(min_sum, curr)
11        
12        return min_sum