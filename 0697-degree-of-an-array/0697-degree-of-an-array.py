class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        t = -1
        val = set()
        num_count = Counter(nums)
        nums_count = sorted(num_count.items(), key=lambda x: x[1], reverse=True)
        for k, v in nums_count:
            if t == -1:
                t = v
            
            if t != v:
                break
            
            val.add(k)
        start = [-1] * (max(nums) + 1)
        end = [-1] * (max(nums) + 1)

        for i in range(len(nums)):
            if start[nums[i]] == -1 and nums[i] in val:
                start[nums[i]] = i

        n = len(nums)
        for j in range(n-1, -1, -1):
            if end[nums[j]] == -1 and nums[j] in val:
                end[nums[j]] = j
        print(start, end)
        res = float("inf")
        for i in range(len(nums)):
            if start[nums[i]] != -1 and nums[i] in val:
                res = min(end[nums[i]]-start[nums[i]] + 1, res)
        return 0 if res == float("inf") else res