class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:     

        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1

            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
                
        duplicates = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.append(nums[i])
        
        return duplicates