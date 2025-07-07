class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return sorted([num for num in count if count[num] > 1])