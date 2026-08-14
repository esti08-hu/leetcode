class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        result = []
        n = len(nums)
        last_added = -1
        for j in range(n):
            if nums[j] == key:
                start = max(0, j - k)
                end = min(n - 1, j + k)
                for i in range(start, end + 1):
                    if i > last_added:
                        result.append(i)
                        last_added = i
        return result