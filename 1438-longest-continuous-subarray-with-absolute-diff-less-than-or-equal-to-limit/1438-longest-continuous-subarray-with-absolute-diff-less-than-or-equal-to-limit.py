class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        Q1 = deque()
        Q2 = deque()
        left = 0
        result = 0

        for right, n in enumerate(nums):
            while Q1 and Q1[-1] > n:
                Q1.pop()
            Q1.append(n)

            while Q2 and Q2[-1] < n:
                Q2.pop()
            Q2.append(n)

            while Q2[0] - Q1[0] > limit:
                if Q1[0] == nums[left]:
                    Q1.popleft()
                if Q2[0] == nums[left]:
                    Q2.popleft()
                left += 1

            result = max(result, right - left + 1)

        return result