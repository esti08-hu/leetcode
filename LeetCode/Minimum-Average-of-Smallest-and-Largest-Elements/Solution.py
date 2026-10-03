1class Solution:
2    def minimumAverage(self, nums: List[int]) -> float:
3        nums.sort()
4        l, r = 0, len(nums) - 1
5        min_ave = float("inf")
6        total = sum(nums)
7        while r > l:
8            ave = (nums[r] + nums[l])/2.0
9            min_ave = min(min_ave, ave)
10            r -= 1
11            l += 1
12
13        return min_ave