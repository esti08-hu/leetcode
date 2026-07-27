class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums3_set = set(nums3)
        
        nums = []
        nums += list(nums1_set)
        nums += list(nums2_set)
        nums += list(nums3_set)

        cnt_nums = Counter(nums)
        res = []
        for k, v in cnt_nums.items():
            if v >= 2:
                res.append(k)

        return res

        