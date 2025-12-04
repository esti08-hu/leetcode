class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        def backtrack(curr_list, idx, s):
            if len(curr_list) == 3 and s == 0:
                res.append(curr_list[:])
                return 
            if len(curr_list) == 3:
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                curr_list.append(nums[i])
                backtrack(curr_list, i+1, s+nums[i])
                curr_list.pop()
        
        backtrack([], 0, 0)
        return res