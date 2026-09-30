1class Solution:
2    def numberGame(self, nums: List[int]) -> List[int]:
3        nums.sort()
4        res = [] 
5        l, r = 0, 1
6
7
8        while r < len(nums):
9            res.append(nums[r])
10            res.append(nums[l])
11            l+=2
12            r+=2
13        return res