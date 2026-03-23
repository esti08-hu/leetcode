class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        count_sort = [0]*(max(nums)+1)

        for n in nums:
            count_sort[n] += 1
        
        nums = []
        for i in range(len(count_sort)):
            if count_sort[i]:
                for j in range(count_sort[i]):
                    nums.append(i)
        
        max_gap = 0

        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
        
        return max_gap