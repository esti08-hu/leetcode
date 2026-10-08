1class Solution:
2    def smallestIndex(self, nums: List[int]) -> int:
3        for i, num in enumerate(nums):
4            curr = num
5            res = 0
6            while curr > 0:
7                rem = curr%10
8                res += rem
9                curr//=10
10            if res == i:
11                return res
12        return -1