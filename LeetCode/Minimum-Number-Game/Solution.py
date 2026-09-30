1class Solution:
2    def numberGame(self, nums: List[int]) -> List[int]:
3        nums.sort()
4        res = [] 
5        l, r = 0, 1
6
7        while r < len(nums):
8            res.append(nums[r])
9            res.append(nums[l])
10            l+=2
11            r+=2
12        return res