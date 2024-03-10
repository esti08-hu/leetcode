class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_nums1 = nums1 if len(nums1) < len(nums2) else nums2
        new_nums2 = nums1 if len(nums1) > len(nums2) else nums2

        nums1 = list(set(new_nums1))
        nums2 = list(set(new_nums2))

        inters = ([n for n in nums1 if n in nums2])

        return inters