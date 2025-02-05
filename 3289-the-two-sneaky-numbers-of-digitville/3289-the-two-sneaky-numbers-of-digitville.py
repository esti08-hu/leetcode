from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        sorted_num = (sorted(nums_count, key=nums_count.get))

        return [sorted_num[-1], sorted_num[-2]]
