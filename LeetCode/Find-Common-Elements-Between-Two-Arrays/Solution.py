1class Solution:
2    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        ans1, ans2 = 0, 0
4        nums1_cnt = Counter(nums1)
5        nums2_cnt = Counter(nums2)
6
7        for k, v in nums1_cnt.items():
8            if k in nums2_cnt:
9                ans1 += nums1_cnt[k]
10                ans2 += nums2_cnt[k]
11        return [ans1, ans2]
12