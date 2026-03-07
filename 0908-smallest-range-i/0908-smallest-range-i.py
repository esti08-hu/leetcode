class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)

        min_num += k
        max_num -= k

        if min_num >= max_num:
            return 0
        return max_num - min_num