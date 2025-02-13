class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        max_len_dig = len(str(max(nums)))

        s_nums = list(map(str, nums))

        max_dig = 0

        def custom_compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        def largestNumber(nums):
            nums_str = list(map(str, nums))
            
            nums_str.sort(key=cmp_to_key(custom_compare))
            
            largest_num = ''.join(nums_str)
            
            if largest_num[0] == '0':
                return '0'
            else:
                return largest_num
        sorted_nums = largestNumber(nums)

        return "".join(map(str, sorted_nums))




