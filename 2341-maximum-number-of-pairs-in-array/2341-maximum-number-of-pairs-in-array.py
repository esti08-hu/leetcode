from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        leftover = 0
        operation = 0
        nums_count = Counter(nums)

        for value in nums_count.values():
            operation += value//2
            leftover += value%2

        return [operation, leftover]