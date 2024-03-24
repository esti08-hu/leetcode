class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_nums = (Counter(nums))
        position = [i for i,val in enumerate(count_nums.values()) if val>=2]
        return (list(count_nums.keys())[position[0]])