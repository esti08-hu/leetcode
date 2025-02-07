class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        size = len(nums)
        count = 0
        for i in range(size - 1):
            for j in range(i+1, size):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count +=1
        
        return count