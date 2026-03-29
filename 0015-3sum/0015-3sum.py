class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            l, r = k+1, len(nums)-1
            while l < r:
                if nums[k] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[k] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return res