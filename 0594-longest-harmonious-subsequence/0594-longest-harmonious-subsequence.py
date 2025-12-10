class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_sub = 0
        for k, v in count.items():
            if k + 1 in count:
                max_sub = max(max_sub, count[k] + count[k+1])
        
        return max_sub
