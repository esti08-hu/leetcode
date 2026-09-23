1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        count = 0
4        for num in nums:
5            if num < k:
6                count += 1
7        
8        return count