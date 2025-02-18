class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_dict = defaultdict(int)
        nums_dict[0] = 1 
        prefixSum = 0
        count = 0
        
        for num in nums:
            prefixSum += num
            count += nums_dict[prefixSum - k]
            nums_dict[prefixSum] += 1
        
        return count