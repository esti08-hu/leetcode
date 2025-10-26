class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist_nums = list(set(nums))
        if len(dist_nums) <= 2:
            return max(dist_nums)
        
        dist_nums.sort(reverse=True)
        return dist_nums[2]