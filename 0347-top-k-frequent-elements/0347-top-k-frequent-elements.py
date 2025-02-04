from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        res = []
        
        freq = []
        for key, value in nums_count.items():
            freq.append((value, key))  

        freq.sort(reverse=True)

        for i in range(k):
            res.append(freq[i][1])

        return res    