class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_cit = sorted(citations)
        max_h = -float("inf")
        for i in range(len(citations)):
            min_v = min(sorted_cit[i], len(sorted_cit[i:]))
            if max_h < min_v:
                max_h = min_v
        return max_h