class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_cnt = Counter(nums)

        return sorted(nums, key=lambda x: (nums_cnt[x], -x))