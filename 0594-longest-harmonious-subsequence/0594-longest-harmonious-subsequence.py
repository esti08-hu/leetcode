class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)

        min_num = nums[0]
        min_idx = 0
        max_sub = 0
        for i in range(1, len(nums)):
            while  nums[i] - min_num > 1:
                min_idx += 1
                min_num = nums[min_idx]
            if nums[i] - min_num == 1:
                max_sub = max(max_sub, i - min_idx + 1) 
            
        return max_sub