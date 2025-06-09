class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        unique_count = len(set(nums))
        count = 0
        freq = {}
        
        left = 0
        for right in range(n):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            while len(freq) == unique_count:
                count += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return count