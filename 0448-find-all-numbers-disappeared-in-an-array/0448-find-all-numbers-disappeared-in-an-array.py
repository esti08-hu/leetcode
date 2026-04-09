class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[nums[i]-1] = nums[i]
        
        ans = []
        for i in range(len(nums)):
            if not res[i]:
                ans.append(i+1)
            
        return ans