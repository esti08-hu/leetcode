class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0]*(len(nums)+1)
        for req in requests:
            l,r = req

            prefix_sum[l] += 1
            prefix_sum[r+1] -= 1

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]
        
        prefix_sum.sort(reverse=True)

        nums.sort(reverse=True)

        max_sum = sum([prefix_sum[i]*nums[i] for i in range(len(nums))])

        return max_sum%(10**9 + 1)