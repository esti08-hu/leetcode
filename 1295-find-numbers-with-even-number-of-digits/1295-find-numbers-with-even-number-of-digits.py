class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        count = 0
        for num in nums:
            if len(num) % 2 == 0:
                count += 1
            
        return count