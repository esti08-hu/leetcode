class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_len_dig = len(str(max(nums)))

        s_nums = list(map(str, nums))

        max_dig = 0
        s_nums = list(map(str, nums))

        sorted_nums = sorted(s_nums, key=lambda x: (x * max_len_dig)[:max_len_dig], reverse=True)
        
        return "".join(map(str, sorted_nums))



