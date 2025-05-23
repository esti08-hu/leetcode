class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        if len(nums1) % 2 == 0:
            return reduce(xor, nums1)
        if len(nums2) % 2 == 0:
            return reduce(xor, nums2)
        return reduce(xor, nums1) ^ reduce(xor, nums2)