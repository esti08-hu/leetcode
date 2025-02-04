from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        res = []
 
        freq = zip(nums_count.values(), nums_count.keys())

        freq = list(freq)

        sorted_freq = sorted(freq, reverse=True)
        
        for i in range(k):
            res.append(sorted_freq[i][1])
        
        return res
