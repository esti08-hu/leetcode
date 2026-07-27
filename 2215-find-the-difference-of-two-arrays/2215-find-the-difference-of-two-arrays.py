class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res = []
        curr = []
        for num in nums1_set:
            if num not in nums2_set:
                curr.append(num)
        res.append(curr)

        curr = []
        for num in nums2_set:
            if num not in nums1_set:
                curr.append(num)
        res.append(curr)

        return res
