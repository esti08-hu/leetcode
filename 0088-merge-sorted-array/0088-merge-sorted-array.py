class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = []
        n2 = []

        for i in range(m):
            n1.append(nums1[i])
        for j in range(n):
            n2.append(nums2[j])

        n1.extend(n2)
        nums1[:] = sorted(n1)