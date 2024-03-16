class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        count_map = {0: -1}  
        
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
            else:
                count -= 1
                
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i
        
        return max_length