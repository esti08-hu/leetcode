class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res = [[],[]]
        
        for num in nums1_set:
            if num not in nums2_set:
                res[0].append(num)

        for num in nums2_set:
            if num not in nums1_set:
                res[1].append(num)

        return res
