class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return False
        sum_list = []
        l,r = 0, 1
        while r < len(nums):
            sum_list.append(nums[l]+nums[r])
            l+=1
            r+=1

        sum_set = set(sum_list)

        if len(sum_set) != len(sum_list):
            return True
        
        else:
            return False