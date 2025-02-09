class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges_list = []
        for r in ranges:
            ranges_list.extend([i for i in range(r[0], r[1]+1)])
        set_ranges_list = set(ranges_list)

        check_nums = [i for i in range(left, right+1)]
        for n in check_nums:
            if n not in set_ranges_list:
                return False

        return True
