class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        start = -1
        frequency = Counter()
        
        for end, num in enumerate(nums):
            frequency[num] += 1
            
            while frequency[num] > k:
                start += 1
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == 0:
                    del frequency[nums[start]]
        
            ans = max(ans, end - start)
        
        return ans