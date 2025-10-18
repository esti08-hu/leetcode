class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_idx = {nums2[i]:i for i in range(len(nums2))}
        res = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            for j in range(nums2_idx[n]+1, len(nums2)):
                if nums2[j] > n:
                    res[i] = nums2[j]
                    break
        return res

