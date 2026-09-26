1class Solution:
2    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
3        count = 0
4        for n1 in nums1:
5            for n2 in nums2:
6                if n1%(n2*k)==0:
7                    count += 1
8        return count