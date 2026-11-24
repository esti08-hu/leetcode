class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_xor = 0
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > nums[left]:
                left += 1
            
            for i in range(left, right + 1):
                max_xor = max(max_xor, nums[i] ^ nums[right])
        
        return max_xor